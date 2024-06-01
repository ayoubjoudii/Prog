from matrice import m,n

print("\n","half left")
for i in range(n):
    print("\t")
    for j in range(n//2):
        print(m[i,j],end=" ")
print("\n","half top")
for i in range(n//2):
    print("\t")
    for j in range(n):
        print(m[i,j],end=" ")
print("\n","half bottom")
for i in range(n//2,n):
    print("\t")
    for j in range(n):
        print(m[i,j],end=" ")
print("\n","half top left")
for i in range(n//2):
    print("\t")
    for j in range(n//2):
        print(m[i,j],end=" ")
print("\n","half bottom left")
for i in range(n//2,n):
    print("\t")
    for j in range(n//2):
        print(m[i,j],end=" ")
