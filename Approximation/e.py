e = 2.718281828459045
ep = 0.00001
def fact(x):
    if x == 0: 
        return 1
    else : 
        return fact(x-1)*x
def euler(ep):
    n = 1
    x = 1
    p = x + 1/fact(n)
    while abs(p-x) > ep:
        x = p
        n += 1
        p = x + 1/fact(n)
    return p
print("e ~",e)
print(euler(ep))