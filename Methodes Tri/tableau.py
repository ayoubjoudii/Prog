from random import randint
from numpy import array 

def exemp():
    t = array([int]*20)
    for i in range(20):
        t[i] = randint(0,90)
    return t 