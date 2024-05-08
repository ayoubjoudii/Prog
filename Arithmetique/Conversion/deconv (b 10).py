def deconv(x,b):
    c = 0
    p = 1
    for i in range(len(x)-1,-1,-1):
        if "0"<=x[i]<="9":
            c = c + int(x[i]) * p
        else : 
            c += (ord(x[i])-55) * p
        p *= b
    return c

print(deconv("MI",30)) #MI 30 = 678