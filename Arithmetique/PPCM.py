def ppcm(a,b): #my way 
    k = 1
    while a != b:
        if (a * k) % b == 0:
            b = a 
        else:
            k+=1
    return a*k
def ppcm1(a,b): 
    i = 1 
    r = a * i
    while r % b != 0 :
        r = a*i
        i += 1
    return r

   
print(ppcm(13,16)) #13 16 = 208
print(ppcm1(13,16)) 
