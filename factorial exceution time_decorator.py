import time
import math
def calculate_time(func):
    def wrapper(n):
        begin = time.time()
        func(n)
        end = time.time()
        print("Time take in :",func.__name__,end - begin)
    return wrapper
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
factorial(10)
    