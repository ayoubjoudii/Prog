def lopt(ep,p):
    l = 0
    s = l * (p - 2*l) / 3.14
    l += ep 
    smax = l * (p - 2*l) / 3.14
    while smax > s and l < p/2 :
        s = smax
        l += ep 
        smax = l * (p - 2*l) / 3.14
    return l 