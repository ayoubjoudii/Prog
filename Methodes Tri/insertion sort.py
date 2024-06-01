from tableau import *

t = exemp()
print(t)
def insertion(t,n):
    for i in range(1,n): 
        print("\n",i,"\n")
        mini = t[i]
        j = i
        while t[j-1] > mini and j>0:
            print(mini)
            t[j] = t[j-1]
            print("place",j,t[j])
            j = j-1
        t[j] = mini
        print("\nfinaly",t)

insertion(t,20)