from PyQt5.uic import *
from PyQt5.QtWidgets import *
from numpy import array


def conta(x):
    ch = ""
    for n in range(3):
        h = ord(x[n])
        ch1 = ""
        while h != 0:
            r = h%16
            h = h//16
            if h>9 : 
                ch1 = chr(r+55) + ch1
            else : 
                ch1 = str(r) + ch1
        ch += ch1
    return ch

def formmatrice(m):
    
    for i in range(40):
        for j in range(40):
            m[i][j] = "FFFFFF"   
    f = open("source.txt","r")
    ch = f.readline()[:-1]
    l = 0
    while ch != "":
        if len(ch) % 3 == 1:
            ch += "  "
        elif len(ch) % 3 == 2:
            ch += " "
        c = 0
        while ch != "":
            m[l][c] = conta(ch[:3])
            ch = ch[3:]
            c += 1
        l +=1
        ch = f.readline()[:-1]
    f.close()
def resultat(m):
    f = open("codes.txt","w")
    for i in range(40):
        ch = ""
        for j in range(40):
            ch += m[j][i]
        f.write(ch+"\n")
    f.close()
def crypter():
    m = array([[int]*40]*40)
    formmatrice(m)
    resultat(m)
    print(m)

def affv():
    f = open("source.txt","r")
    ch = f.read()
    w.listv.clear()
    w.listv.addItem(ch)
    f.close()
def affp():
    f = open("codes.txt","r")
    ch = f.read()
    w.listp.clear()
    w.listp.addItem(ch)
    f.close()
def fermer():
    w.close()
def effa():
    w.listv.clear()
    w.listp.clear()
app=QApplication([])
w=loadUi("Interface _sténographie.ui")
w.show()
w.avc.clicked.connect(affv)
w.apc.clicked.connect(affp)
w.crypter.clicked.connect(crypter)
w.eff.clicked.connect(effa)
w.ferm.clicked.connect(fermer)
app.exec_()



