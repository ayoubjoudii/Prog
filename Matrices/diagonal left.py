from matrice import m,n

print("\n","half left")
for i in range(n):
    print("\t")
    for j in range(n//2):
        print(m[i,j],end=" ")
print("\n\n","half top")
for i in range(n//2):
    print("\t")
    for j in range(n):
        print(m[i,j],end=" ")
print("\n\n","half bottom")
for i in range(n//2,n):
    print("\t")
    for j in range(n):
        print(m[i,j],end=" ")
print("\n\n","half top left")
for i in range(n//2):
    print("\t")
    for j in range(n//2):
        print(m[i,j],end=" ")
print("\n\n","half bottom left")
for i in range(n//2,n):
    print("\t")
    for j in range(n//2):
        print(m[i,j],end=" ")
print("\n\n","bottom left diagonal")
for i in range(n):
    print("\t")
    for j in range(i+1):
        print(m[i,j],end=" ")
print("\n\n","top left diagonal")
for i in range(n):
    print("\t")
    for j in range(n-i):
        print(m[i,j],end=" ")

