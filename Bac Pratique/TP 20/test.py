from numpy import array
def conta(x):
    ch = ""
    for n in range(3):
        h = ord(x[n])
        ch1 = ""
        while h != 0:
            r = h%16
            h = h//16
            if h>9 : 
                ch1 = chr(r+55) + ch1
            else : 
                ch1 = str(r) + ch1
        ch += ch1
    return ch
m = array([[int]*40]*40)
f = open("source.txt","r")
ch = f.readline()[:-1]
l = 0
while ch != "":
    if len(ch) % 3 == 1:
        ch += "  "
    elif len(ch) % 3 == 2:
        ch += " "
    c = 0
    while ch != "":
        m[l][c] = conta(ch[:3])
        ch = ch[3:]
        c += 1
    l +=1
    ch = f.readline()[:-1]