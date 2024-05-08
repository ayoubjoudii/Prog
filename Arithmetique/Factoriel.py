def fact1(n):
    if n == 0 :
        return 1 
    else : 
        return n * fact1(n-1)

def fact2(n):
    for i in range(1,n):
        n *= i
    return n

print(fact1(5))
print(fact2(5))