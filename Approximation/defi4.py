from random import randint
ep = 0.001
def fact(x):
    if x == 0:
        return 1 
    else : 
        return x * fact(x-1)
def comb(p,n):
    if p == 0 or p == n :
        return 1
    else : 
        return fact(n) // (fact(p) * fact(n-p))
def puis(x,y):
    if y == 0:
        return 1
    else : 
        return x * puis(x,y-1)
def eps(ep):
    x = randint(4,8)
    f = 1
    s = f + 2 * (x/(3 * comb(1,2)))
    n = 2
    y = 5
    sig = 1
    for i in range(12):
        f = s 
        sig = -sig
        s = f + sig * puis(2,n) * ( puis(x,n)/(y * comb(n,n*2)))
        n += 1
        y += 2
    return s

print(eps(ep))