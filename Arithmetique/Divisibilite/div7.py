def div(n):
    ch = "132"
    n = str(n)
    while len(n) > 1:
        i = len(n)
        sig = 1
        k = 0
        x = 0
        while i > 0 :
            i = i-1
            x = x + int(n[i])*(int(ch[k])*sig)
            k = k +1 
            if k == 3: 
                sig = -sig
                k = 0
        n = str(x)
    return n == "0" or n == "7"

print(div(7))