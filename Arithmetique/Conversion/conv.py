#convert all
def conv(x,b):
            c = ""
            xr = "0123456789ABCDEF"
            while x != 0:
                r = x%b
                x = x//b
                c = xr[r] + c
            return c
print(conv(10,8)) #12 