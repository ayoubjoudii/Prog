from math import *

def f(x):
    return x*sin(x)*sin(x)

ep = 0.001
x = 1
while abs(x-f(x)) >ep : 
    x = f(x)

print(f(x))