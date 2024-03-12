def palind(ch):
    if len(ch)<= 1 :
        return True
    elif ch[0] != ch[-1]:
        return False 
    else : 
        return palind(ch[1:len(ch)-1])
    
print(palind("radar"))