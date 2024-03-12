n = 300
a = 0 
b = 2
k = 2
def puis(x,y):
    p = 1
    for i in range(y):
        p = p * x
    return p 
def f(x): 
    return -7/4 * puis(x,4) + 5 * puis(x,3) - 4 * x + 4
def rect(n):
    h = (b-a)/n #3orth ta9sima
    x = a # a gauche
    # a droite : x = a+h 
    # au milieu : x = a + h/2 , tawa hetha info ? 
    s = 0
    for i in range(n): 
        s = s + f(x)
        x = x + h
    return s*h 
def trap(n): # hethi ada9
    h = (b-a)/n
    x = a
    s = 0
    for i in range(n): 
        s = s + (f(x) + f(x+h))/2 # misa7et trapeze : (kbira + s8ira) / 2 * irtife3
        x = x + h
    return s*h 

print(trap(n))