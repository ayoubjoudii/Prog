def fact(n):
    if n == 0 :
        return 1
    else : 
        return n * fact(n-1)
def A(n,p):
    return fact(n) // fact(n-p)
               #  p
print(A(7,4)) # A n -- A(7,4) = 840