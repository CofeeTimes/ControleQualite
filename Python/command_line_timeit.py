import math

def example(x):
    mylist = []
    mylist.append(x)
    for x in range(100):
        mylist.append(math.sqrt(x))

# test with: 
        # python -m timeit -n 10000 --setup="from command_line_timeit import example;x=10" "example(x)"