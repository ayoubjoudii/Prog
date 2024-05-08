def prem(n):
    test = True
    for i in range(2,n//2+1):
        if n % i == 0:
            test = False 
    return test

print(prem(4))

