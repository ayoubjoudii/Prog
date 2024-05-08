def factprem(n):
    ch = ""
    i = 2
    while n >= i :
        if n % i == 0:
            ch += str(i)+"*"
            n = n//i 
        else : 
            i += 1

    return ch[:-1]

print(factprem(630)) #300 = 2*2*3*5*5