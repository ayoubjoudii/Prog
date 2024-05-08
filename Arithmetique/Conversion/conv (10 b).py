#convert all
def conv(x,b):
            c = ""
            while x != 0:
                r = x%b
                x = x//b
                if r > 9 :
                    c = chr(r+55) + c
                else:
                    c = str(r)+c   
            return c
print(conv(678,30)) #678 30 = MI 