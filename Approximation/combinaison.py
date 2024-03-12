def fact(x):
    if x == 0:
        return 1 
    else :
        return x*fact(x-1)

def comb(p,n):
    if p == 0 or p==n:
        return 1
    return fact(n)//(fact(p)*fact(n-p))

def comb2(p,n):
    if p == 0 or p == n:
        return 1
    else : 
        return comb2(p-1,n-1) + comb2(p,n-1)

print(comb2(2,4))
