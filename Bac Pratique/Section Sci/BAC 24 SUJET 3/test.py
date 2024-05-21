def puis(x,y):
    p = 1 
    for i in range(y):
        p = p*x
    return p
 
x = 524
n = 1 
if len(x)%2 == 1:
    ch = str(x) + "1"
    for i in range(0,len(ch)-1,2):
        print(ch[i],ch[i+1])
        if ch[i]+ch[i+1] != "00":
            n = n * puis(int(ch[i]) , int(ch[i+1]))
else: 
    ch = str(x)
    for i in range(0,len(ch)-1,2):
        if ch[i]+ch[i+1] != "00":
            n = n * puis(int(ch[i]) , int(ch[i+1]))
print(n)