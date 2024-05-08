ep = 0.0001 
def puis(x,y):
    if y == 0 :
        return 1 
    else : 
        return x * puis(x,y-1)
def fact(n):
    if n == 0 :
        return 1 
    else : 
        return n * fact(n-1)
def exp(n, ep):
    up = 1
    u = up + n/1
    p = 1
    while abs(u-up) > ep : 
        up = u
        p += 1 
        u = up + puis(n,p) / fact(p)
    return u
print(exp(2,ep)) #2 : 7.389056099