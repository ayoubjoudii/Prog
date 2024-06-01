from matrice import m,n

for i in range(n):
    print("\t")
    for j in range(1,n):
        print(m[i,n-j],end=" ")
