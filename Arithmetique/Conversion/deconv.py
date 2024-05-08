#deconvert all

def deconv(x,b):
    def puis(x,y):
        if y == 0:
            return 1
        else:
            return x*puis(x,y-1)
    c = 0
    for i in range(len(x)-1,-1,-1):
        if "0"<=x[i]<="9":
            c = c + int(x[i]) * puis(b,len(x)-1-i) 
        else : 
            c += (ord(x[i])-55) * puis(b,len(x)-1-i)
    return c

print(deconv("1010",2)) #547