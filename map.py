#Functions to create map objects
import matplotlib.pyplot as plt
import math
import random
import timer as timer

def makeRandomBuilding(n, pos = (0,0), size = 5.0):
    if n <= 2.0:
        raise ValueError('n must be greater than 2')
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    
    thetas = [random.uniform(0,2*math.pi) for i in range(n)]
    thetas = sorted(thetas)
    thetas.append(thetas[0])

    Xs = [size * math.cos(theta) + pos[0] for theta in thetas]
    Ys = [size * math.sin(theta) + pos[1] for theta in thetas]

    return (Xs, Ys)

def makeRegularBuilding(n, pos = (0,0), size = 5.0, rot = 0.0):
    if n <= 2.0:
        raise ValueError('n must be greater than 2')
    if not isinstance(n, int):
        raise TypeError('n must be an integer')

    thetas = [i * 2 * math.pi / n - rot for i in range(n)]
    thetas.append(thetas[0])

    Xs = [size * math.cos(theta) + pos[0] for theta in thetas]
    Ys = [size * math.sin(theta) + pos[1] for theta in thetas]

    return (Xs, Ys)


def drawBuilding(vertices, figure = 1):
    Xs, Ys = vertices

    plt.figure(figure)
    plt.plot(Xs, Ys, color = 'k')

if __name__ == '__main__':
    timer.time_function(makeRandomBuilding, 3)