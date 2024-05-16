import math
def premier(n):
    test = True
    for i in range(2,n//2 + 1):
        if n % i == 0 :
            return False    
    return test
up = 1 
u = up - 1/5 
sig = 1  
k =7
while abs(u - up) > 0.0001 :
    if premier(k):
        up = u
        u = up + (1/k)*sig
        sig = -sig
    k = k +1
print(u*2*math.sqrt(3))