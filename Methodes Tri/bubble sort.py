from tableau import * 

t = exemp()
print(t)
def bulle(t,n):
    for i in range(n):
        print(i)
        for j in range(n-1):
            print("old",t[j],t[j+1])
            if t[j] > t[j+1]:
                temp = t[j]
                t[j] = t[j+1]
                t[j+1] = temp
                print("new",t[j],t[j+1])
    # print(t)

bulle(t,20)