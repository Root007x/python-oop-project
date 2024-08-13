import math

def timer(func):
    def inner():
        print("Time Started")
        func()
        print("Time Ended")
    return inner



#timer()()

@timer # time(get_factorial)() same 
def get_factorial():
    print("Factorial Starting")
    

get_factorial()