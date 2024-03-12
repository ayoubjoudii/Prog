def fact(x):
    if x == 0 : 
        return 1 
    else : 
        return fact(x-1)*x
def arr(n,p):
    return fact(n)//fact(n-p)

print(arr(4,2))