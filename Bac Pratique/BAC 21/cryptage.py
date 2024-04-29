from PyQt5.QtWidgets import * 
from PyQt5.uic import *
from numpy import array

def codee(nb):
    mot = ""
    while nb != 0 : 
        r = nb % 3
        if r == 0 :
            y = "MA"
        elif r == 1 :
            y = "DES"
        elif r == 2 :
            y = "SON"
        mot = y + mot 
        nb = nb // 3
    return mot
def conv(n):
    ch = "0123456789ABCDEF" 
    s = 0
    p = 1
    for i in range(len(n)-1,-1,-1):
        s += ch.find(n[i]) * p 
        p *= 16
    return s
def generer():
    f  = open("imghexa.txt" , "r")
    t = array([nm] * 30)
    ch = f.readline()
    size = 0      
    while ch != "":
        n = ch[:2]
        t[size] = dict(nm)
        t[size]["hex"] = n
        t[size]["num"] = size+1
        t[size]["dec"] = conv(n)
        size += 1 
        ch = f.readline()
    test = True
    while test :
        test = False
        for i in range(size-1):
            if t[i]["dec"] > t[i+1]["dec"]:
                temp = t[i]["dec"]
                temp1 = t[i]["num"]
                temp2 = t[i]["hex"]
                t[i]["dec"] = t[i+1]["dec"]
                t[i]["num"] = t[i+1]["num"]
                t[i]["hex"] = t[i+1]["hex"]
                t[i+1]["dec"] = temp
                t[i+1]["num"] = temp1
                t[i+1]["hex"] = temp2
                test = True
    ft = open("resultat.txt","w")
    w.table.setRowCount(0)
    for i in range(size):
        c = codee(t[i]["dec"])
        ft.write(c+" "+str(t[i]["dec"])+"\n")
        w.table.insertRow(i)
        w.table.setItem(i, 0 , QTableWidgetItem(str(t[i]["dec"])))
        w.table.setItem(i, 1 , QTableWidgetItem(c))
    

    
        
nm = {
    "hex" : str,
    "num" : int, 
    "dec": int
}
app = QApplication([])
w = loadUi("hex.ui")
w.show()
w.gen.clicked.connect(generer)
app.exec_()