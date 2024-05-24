f = open("phrases.txt","r")
ch = f.readline()[:-1]
while ch != "":
    ch1 = ch.strip()
    while ch1.find("  ") != -1:
        p = ch1.find("  ")
        ch1 = ch1[:p] + ch1[p+1:]
    ch = f.readline()[:-1]
    print(ch1)