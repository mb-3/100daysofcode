import time


def speed_calc_decorator(function):

    def speed_read():
        time_start = time.time()
        function()
        time_end = time.time()
        print(f"{function.__name__} run speed: {time_end - time_start}")
        
    return speed_read

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
