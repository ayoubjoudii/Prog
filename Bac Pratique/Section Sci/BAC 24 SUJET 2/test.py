x = "051015202530"


n = int(x[2:4]) - int(x[0:2]) 
i = 4
while i<len(x)-3 and n!= 0:
    if (int(x[i+2:i+4]) - int(x[i:i+2]) != n):
        n = 0
    else : 
        n = int(x[i+2:i+4] ) -int(x[i:i+2]) 
    i = i+2