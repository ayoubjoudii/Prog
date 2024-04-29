from PyQt5.QtWidgets import * 
from PyQt5.uic import * 

def premier(ch):
    n  = int(ch[0:3])
    test = True 
    for i in range(2,n):
        if n % i == 0 and n!= 2:
            test = False
    return test  
def binaire(ch):
    n = int(ch[3:8])
    ch = ""
    while n > 0 :
        r = n%2 
        n = n //2
        ch = str(r) + ch 
    s = 0 
    for i in range(len(ch)):
        if ch[i] == "0":
            s += 1
    return s>8
def div(ch):
    d = int(ch[0:3])
    n = int(ch[8:])
    return n % d == 0

def verifier():
    ch = w.edit.toPlainText()
    w.list.clear()
    f = open("codes.txt", "r")
    lin = f.readline()
    valid = True 
    if len(ch) != 13 or not(premier(ch)) or not(binaire(ch)) or not(div(ch)) :
        valid = False
    else:
        test = False 
        while lin != "" and test == False :
            if int(ch) == int(lin) : 
                test = True
            lin = f.readline()
    if valid == False :
        w.list.addItem(ch + ": est non valide")
    elif test == False :
        w.list.addItem(ch + ": est deja utilisee")
    else : 
        w.list.addItem(ch + ": est valid")

app = QApplication([])
w = loadUi("codes.ui")
w.show()
w.verifier.clicked.connect(verifier)
app.exec_()