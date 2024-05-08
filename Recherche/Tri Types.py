from numpy import array
T1 = array([5,13,44,8,4,2,9,16,19,7,2,10])
T2 = array([1,2,3,7,5,4,17,2,8,18,0,9])
def selection(T1):
    k = True
    while k :
        k = False
        for i in range(len(T1)-1):
            if T1[i]>T1[i+1]:
                x = T1[i]
                T1[i] = T1[i+1]
                T1[i+1] = x
                k = True
        
    print(T1)
def insertion(T1):
    pass
def bulle(T1):
    maxp = 0
    for i in range(len(T1)):
        for j in range(i,len(T1)):
            print(j,T1[maxp])
            if T1[j] > T1[maxp]:
                maxp = j
        temp = T1[i]
        T1[i] = T1[maxp]
        T1[maxp] = temp
    print(T1)

bulle(T1)