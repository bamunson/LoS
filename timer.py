#Functions to help with timing
import time

def time_function(function, *args):
    times = {'nanoseconds': 1e-9, 'microseconds': 1e-6, 'milliseconds': 1e-3, 'seconds': 1}
    t1 = time.time()
    function(*args)
    t2 = time.time()

    time_elapsed = t2 - t1
    for unit, threshold in times.items():
        if time_elapsed < threshold:
            n = int(10/threshold)
            t3 = time.time()
            [function(*args) for _ in range(n)]
            t4 = time.time()
            time_per_loop = (t4 - t3) / n
            print(f'Ran {n} times. Took {(time_per_loop/threshold):.5f} {unit} to run')
            return

    print(f'Ran 1 time. Took {time_elapsed:.4f} seconds to run')