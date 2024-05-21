y = "5527579822"#"967445987"

ch = ""
for i in range(len(y)):
    ch = ch + str(int(y[i])%7)
y = ch

z = ""
if len(y) % 2 != 0:
    y = y[1:]
    for i in range(len(y)-1,-1,-2):
        z = str(int(y[i-1]+y[i])%7) +z
    print(y[0]+z)
else:
    for i in range(len(y)-1,-1,-2):
        z = str(int(y[i-1]+y[i])%7) +z
    print(z)
