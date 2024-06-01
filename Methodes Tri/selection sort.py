from tableau import *
t = exemp()
def selection(t,n):
    for i in range(n): 
        print("\n",i,"\n")
        mini = i
        for j in range(i+1,n):
            if t[j] < t[mini] :
                mini = j 
        if mini != i :
            temp = t[mini]
            t[mini] = t[i]
            t[i] = temp
        print(t)

selection(t,20)