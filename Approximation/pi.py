import math 
ep = 0.00001
pi = 3.14159
#wallis : pi/2 = (2/1)*(2/3)*(4/3)*(4/5)*(6/5)*(6/7)*(...)
#Euler  : (pi^2)/6 = 1+ 1/2^2 + 1/3^2 + ...
def wallis(ep):
    n = 2
    d = 3
    f = n
    s = f*n/d
    while abs(f-s) > ep : 
        if d < n : 
            d += 2
        else: 
            n += 2
        f = s
        s = (n/d) * f
    return s*2
def euler(ep):
    x = 1
    n = 2
    s = x + 1/(n*n)
    while abs(math.sqrt(x*6)-math.sqrt(s*6)) > ep:
        x = s 
        n += 1
        s = x + 1/(n*n)
    return math.sqrt(s*6)
print("π ~",pi)
print(" Wallis :",wallis(ep))  
print(" Euler :",euler(ep))  
