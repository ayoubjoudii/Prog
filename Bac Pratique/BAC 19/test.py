from numpy import array

def puis(a, b):
    if b == 0:
        return 1
    else:
        return a * puis(a, b - 1)


def ppcm(a, b):
    t1 = array([eng]*10)
    t2 = array([eng]*10)
    p = 2
    i = 0
    while a > 1:
        if a % p ==0 :
            nb = 0
            while a % p == 0:
                a = a // p
                nb += 1
            t1[i] = dict(eng)
            t1[i]["n"] = p
            t1[i]["p"] = nb
            i += 1
        else:
            p+= 1 
    
    
    p2 = 2
    i2 = 0
    while b > 1:
        if b % p2 ==0 :
            nb = 0
            while b % p2 == 0:
                b = b // p2
                nb += 1
            t2[i2] = dict(eng)
            t2[i2]["n"] = p2
            t2[i2]["p"] = nb
            i2 += 1
        else:
            p2+= 1 
    
    
    
    s = 1
    for f in range(i):
        prime1 = t1[f]["n"]
        power1 = t1[f]["p"]
        primein2 = False
        for g in range(i2):
            if t2[g]["n"] == prime1:
                primein2 = True
                powerin2 = t2[g]["p"]
        if primein2:
            if power1 > powerin2 :
                s *= puis(prime1, power1) 
            else:
                s *= puis(prime1, powerin2) 
        else:
            s *= puis(prime1, power1)

    for f in range(i2):
        prime2 = t2[f]["n"]
        power2 = t2[f]["p"]
        primein1 = False
        for g in range(i):
            if t1[g]["n"] == prime2:
                primein1 = True
        if not primein1:
            s *= puis(prime2, power2)
    return s


eng = {
    "n" : int,
    "p" : int
}

