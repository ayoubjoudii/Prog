#div all
def div(n,b):
    while n >= b:
        n = n - b
    return(n == 0)

print(div(5,5))
