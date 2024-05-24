def palind(ch):
    if len(ch)<= 1 :
        return True
    elif ch[0] != ch[-1]:
        return False 
    else : 
        return palind(ch[1:len(ch)-1])
    
def palind1(ch):
    ch1 =""
    for i in range(len(ch)):
        ch1 = ch[i] +ch1

    return ch1==ch
    
print(palind1("radar"))