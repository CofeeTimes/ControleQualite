import timeit

mysetup='''
from math import sqrt
x = 10
def example(x):
    mylist = []
    mylist.append(x)
    for x in range(100):
        mylist.append(sqrt(x))
'''

mycode = "example(x)"
print(timeit.timeit(setup = mysetup, stmt = mycode, number = 10000))