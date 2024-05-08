def puis(a,b):
    if b == 0 :
        return 1
    else : 
        return a * puis(a,b-1)
    
def puis1(a,b): 
    p = 1 
    for i in range(b):
        p = p*a
    return p


print(puis(2,3))
print(puis1(2,3))