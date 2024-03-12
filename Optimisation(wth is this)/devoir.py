import math
ep = 0.000001
def g(x):
    return math.sin(x) + 3
def approch(ep): # point fixe
    x = 0
    while abs(g(x) - x) > ep:
        x  = g(x)
    return x
def subdiv(k,N): # calcul air
    h = k/N #3orth l ta9sima N  
    s = 0 #misa7a li tabda beha 
    x = 0 + h/2 #chtar l 3orth bch kol matzid tehseb be chtar, ti chbih haka wala l info
    for i in range(1,N):
        s = s + h*g(x) # surface ta9sima
        x = x + h # zedt kadamt b h
    return s - ((k*k)/2) # na7a surface triangle k 9a3da w irtife3 / 2