from pickle import dump,load
def conv(n,b):
    ch = ""
    while n != 0 :
        r = n % b
        n= n// b
        if r > 9 : 
            ch = chr(r+55) + ch 
        else : 
            ch = str(r) + ch 
    return ch 
def bres(c):
    p = c[0]
    test = len(c) > 1 
    for i in range(1,len(c)):
        if c[i] != p :
            test = False 
    return test 
def genbres():
    f = open("nombres.txt","r")
    fb = open("bresilien.dat","wb")
    ch = f.readline()
    while ch != "":
        for b in range(2,17):
            c = conv(int(ch),b)
            if bres(c) and b < int(ch)-2 :
                e = dict(en)
                e["n"] = int(ch)
                e["b"] = b
                e["rep"] = c
                dump(e,fb)
        ch = f.readline()
    





en = {
    "n" : int,
    "b" : int,
    "rep" : str
}
genbres()

fb = open("bresilien.dat","rb")

test = True 
while test : 
    try : 
        x = load(fb)
        print(x["n"],x["b"],x["rep"])
    except:
        test = False 
