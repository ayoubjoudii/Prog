from matrice import m,n

print("\n","half right")
for i in range(n):
    print("\t")
    print(" "*(n//2),end="   ")
    for j in range(n//2,n):
        print(m[i,j],end=" ")


print("\n\n","half top right")


for i in range(n//2):
    print("\t")
    print(" "*(n//2),end="   ")
    for j in range(n//2,n):
        print(m[i,j],end=" ")


print("\n\n","half bottom right")


for i in range(n//2,n):
    print("\t")
    print(" "*(n//2),end="   ")
    for j in range(n//2,n):
        print(m[i,j],end=" ")


print("\n\n","bottom right diagonal")


for i in range(n):
    print("\t")
    print("   "*(n-1-i),end="")
    for j in range(n):
        if j >= n-1-i : 
            print(m[i,j],end=" ")


print("\n\n","top right diagonal")


for i in range(n):
    print("\t")
    print("   "*(i),end="")
    for j in range(i,n):
        print(m[i,j],end=" ")



