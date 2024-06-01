from tableau import * 
t = exemp()
print(t)
def shell(t,n):
    p = 0
    while p <n:
        p = p*3+1
    while p != 0:
        p = p // 3
        for i in range(p,n):
            v = t[i]
            j = i
            while j>p-1 and t[j-p] > v :
                t[j] = t[j-p]
                j = j-p
            t[j] = v
    print(t)
shell(t,20)