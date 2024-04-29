from PyQt5.QtWidgets import * 
from PyQt5.uic import * 

def ajouter():
    f =open("nombre.txt" , "a") 
    ch = w.text.text()
    if not(ch.isnumeric() and int(ch) >= 0 )  :
        QMessageBox.critical(w,"erruer","doit etre un entier naturel")
    else : 
        f.write(ch+"\n")
def div13(n):
    s = 0 
    sig = -1
    while len(n) >= 3:
        v = int(n[len(n)-3:])
        s += v * sig
        sig = -sig
        n = n[:len(n)-3]
    if n != "":
        v = int(n)
        s += v * sig
    return abs(s) % 13 == 0

def div7(n) : 
    ch = "132"
    while len(n)>1:
        i = len(n)
        s = 0
        sig = 1 
        k = 0
        while i > 0:
            i -= 1
            s += int(n[i]) * int(ch[k]) * sig
            k += 1
            if k == 3 :
                k = 0 
                sig = -sig
        n = str(s)
    return n == "0" or n == "7" 

def verif():
    f = open("nombre.txt" , "r")
    fa = open("div13.txt" , "w")
    fb = open("div7.txt" , "w")
    ch = f.readline()
    w.div13.clear()
    w.div7.clear()
    while ch != "":
        if div13(ch[:-1]):
            w.div13.addItem(ch)
            fa.write(ch+"\n")
        elif div7(ch[:-1]):
            w.div7.addItem(ch)
            fb.write(ch+"\n")
        ch = f.readline()

app = QApplication([])
w = loadUi("nombre.ui")
w.show()
w.ajouter.clicked.connect(ajouter)
w.verif.clicked.connect(verif)
app.exec_()