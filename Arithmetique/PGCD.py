def pgcd(a,b):
    while a != b :
        if a >= b :
            a -= b 
        else : 
            b -= a
    return a 
def pgcd1(a,b):
    while b != 0 :
        x = a
        a = b
        b = x % b # or a, b = b, a % b thats cool
    return a 
def pgcd2(a,b): 
    if a==b:
        return a 
    elif a>b:
        return pgcd2(a-b,b)
    else:
        return pgcd2(b,b-a)
print(pgcd(120,50))  # 120 50 = 10
print(pgcd1(120,50))
print(pgcd2(120,50))