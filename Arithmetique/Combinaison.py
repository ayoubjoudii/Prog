def fact(n):
    if n == 0 :
        return 1 
    else : 
        return n * fact(n-1)
def C(n,p):
    return fact(n) //(fact(p) * fact(n-p))

print(C(7,4)) #c(7,4) = 35