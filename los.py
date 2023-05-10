#Functions for computing LOS
import map as m
import math
import matplotlib.pyplot as plt
from timer import time_function

def getLinesFromBuilding(vertices):
    Xs, Ys = vertices

    lines = []
    for i in range(len(Xs) - 1):
        x0 = Xs[i]
        y0 = Ys[i]
        dx = Xs[i+1] - Xs[i]
        dy = Ys[i+1] - Ys[i]
        lines.append([x0,dx,y0,dy])
    
    return lines

def getLinesFromAllBuildings(buildings):
    allLines = [line for building in buildings for line in getLinesFromBuilding(building)]
    return allLines

def makeRay(pos, orientation):
    x0, y0 = pos
    dx = math.cos(orientation)
    dy = math.sin(orientation)
    return [x0,dx,y0,dy]

def makeRayField(pos, n_rays, angle_start = 0.0, angle_end = 2*math.pi):
    x0, y0 = pos
    thetas = [i * (angle_end-angle_start) / n_rays + angle_start  for i in range(n_rays)]
    dxs = [math.cos(theta) for theta in thetas]
    dys = [math.sin(theta) for theta in thetas]

    return [[x0, dx, y0, dy] for dx, dy in zip(dxs, dys)]

def plotRays(rays, figure = 1, extent = 1000):
    plt.figure(figure)
    for ray in rays:
        x0,dx,y0,dy = ray
        plt.plot([x0, x0+dx*extent], [y0, y0+dy*extent], 'r')

def findCollision(line1, line2):
    x01, dx1, y01, dy1 = line1
    x02, dx2, y02, dy2 = line2

    num = dx1*(y01-y02) + dy1*(x02-x01)
    den = dy2*dx1 - dx2*dy1

    if den == 0:
        t2 = float("inf")
    else:
        t2 = num/den
    t1 = (x02-x01+dx2*t2)/dx1

    if 0 <= t2 <= 1 and t1 >=0:
        return (t1, t2)
    else:
        return

def collisionCoordinate(t, line):
    x0, dx, y0, dy = line
    return (x0+dx*t, y0+dy*t)

def traceRay(ray, obstacles):
    collisions = [findCollision(ray, obstacle) for obstacle in obstacles]
    first_collision = float("inf")
    for collision in collisions:
        if collision is None:
            continue
        if collision[0] < first_collision:
            first_collision = collision[0]
    return collisionCoordinate(first_collision, ray)

def traceAllRays(rays, obstacles):
    all_collisions = [traceRay(ray, obstacles) for ray in rays]
    return all_collisions

def plotTracedRays(rays, obstacles, figure = 1, extent = 1000):
    collisions = traceAllRays(rays, obstacles)
    plt.figure(figure)
    for obstacle in obstacles:
        x0, dx, y0, dy = obstacle
        plt.plot([x0, x0+dx], [y0, y0+dy], 'k')
    for ray, collision in zip(rays,collisions):
        x0, dx, y0, dy = ray
        if abs(collision[0]) == float("inf"):
            plt.plot([x0, x0+dx*extent], [y0, y0+dy*extent], 'r')
        else:
            plt.plot([x0, collision[0]],[y0, collision[1]],'r')
            plt.plot(*collision,'b.')

if __name__ == '__main__':
    positions = [(7,2),(-5,5),(-8,-10),(2,-1)]
    buildings = [m.makeRandomBuilding(4, p, 3) for p in positions]

    rays = makeRayField((0,0), 2000, 0, 2*math.pi)
    obstacles = getLinesFromAllBuildings(buildings)
    #time_function(traceAllRays, rays, obstacles)
    plotTracedRays(rays, obstacles)
    plt.plot(0,0, 'gs', markersize=10)
    plt.axis('square')
    plt.show(block=True)
