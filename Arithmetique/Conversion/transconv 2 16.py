def conv10(n):
    x = 0
    p = 1
    for i in range(len(n)-1,-1,-1):
        x += int(n[i]) * p
        p *= 2
    return x
def conv16(n):
    ch = ""
    chx = "0123456789ABCDEF"
    while n % 16 != 0 :
        r = n%16 
        n = n//16
        ch = chx[r] + ch 
    return ch 
# def conv2_16(n):
#     ch = ""
#     while len(n) % 4 != 0 :
#         n = "0" + n
#     p = 0
#     for i in range(4,len(n)+1,4):
#         x = n[p:i]
#         p += 4
#         c = conv10(x) 
#         if c > 9 :
#             ch += conv16(c)
#         else : 
#             ch += str(c)
#     return ch
def conv2_16(n):
    while len(n)%4 != 0 :
        n = "0" + n
    ch = ""
    while n != "":
        x = n[:4]
        c = conv10(x)
        if c > 9 :
            ch += chr(c+55)
        else : 
            ch += str(c)
        n = n[4:]
    return ch


print(conv2_16("10101110001111"))
        


