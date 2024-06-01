from tableau import * 

t = exemp()
print(t)
def bulle(t,n):
    for i in range(n): 
        print("\n",i,"\n")
        for j in range(n-1):
            print(t[j],end=" ")
            if t[j] > t[j+1]:
                temp = t[j]
                t[j] = t[j+1]
                t[j+1] = temp
        print("\n",t)

bulle(t,20)