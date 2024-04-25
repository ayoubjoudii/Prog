t = open("chance.txt","r")
def somme(ch):
    
    s = 0
    for i in range(0,len(ch)):
        s = s+int(ch[i])
    while s > 9 :
        x = str(s)
        s = 0
        for i in range(0,len(x)):
            s = s+int(x[i])
    p = t.readline()
    while p != "":
        if int(p) == s :
            return True
        p = t.readline()
    return False

print(somme("80617081"))