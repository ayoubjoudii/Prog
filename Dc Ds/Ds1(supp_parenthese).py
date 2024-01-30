def supp_parenthese(ch,i,p):
    if i == -1 :
        return ch
    elif ch[i] == ')' :
        return supp_parenthese(ch,i-1,i)
    elif ch[i] == "(" :
        return supp_parenthese(ch[0:i]+ch[p+1:len(ch)],i-1,p)
    else :
        return supp_parenthese(ch,i-1,p)

print(supp_parenthese("hello(deleted)whend no this is (deleted lol)",len("hello(deleted)whend no this is (deleted lol)")-1,0))