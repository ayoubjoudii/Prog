def div13(n):
    s = 0 
    sig = -1
    while len(n) >= 3:
        v = int(n[len(n)-3:])
        s += v * sig
        sig = -sig
        n = n[:len(n)-3]
    v = int(n)
    s += v * sig
    return abs(s) % 13 == 0