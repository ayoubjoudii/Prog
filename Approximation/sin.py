ex = 3.1415926535897/2
ep = 0.0000000001 
# sin(x) = x - x^3/3! + x^5/5! - ...
def puis(x,y):
    if y == 0 :
        return 1
    else : 
        return x*puis(x,y-1)
def fact(x):
    if x == 0:
        return 1
    else : 
        return x * fact(x-1)


def sin(x,ep):
    f = x
    n = 3
    s = f - puis(x,n)/fact(n)
    sig = 1
    while abs(f-s) > ep:
        f = s 
        n += 2
        s = f + sig*puis(x,n)/fact(n)
        sig = -sig
    return s 

print("sin(π/2) : 1")
print(sin(ex,ep))