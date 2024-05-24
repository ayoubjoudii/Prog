from PyQt5.uic import * 
from PyQt5.QtWidgets import *

def enr():
    ch = w.mess.toPlainText()
    if ch == "":
        QMessageBox.critical(w,"erreur","chaine vide")
    else:
        f = open("phrases.txt","a")
        f.write(ch+"\n")
        f.close()
        QMessageBox.information(w,"succes","succes enreigstres")

def corig():
    f = open("phrases.txt","r")
    ft = open("phrasescor.txt","w")
    ch = f.readline()[:-1]
    while ch!="":
        ch1 = ""
        ch = ch.strip()
        for i in range(len(ch)-1):
            if ch[i] == " ":
                if ch[i+1] != " ":
                    ch1 += ch[i]
            else : 
                ch1 += ch[i]
        ch1 += ch[-1]
        if ch1[:-1] != ".":
            ch1 += "."
        ft.write(ch1+"\n")
        w.corr.addItem(ch1)
        ch = f.readline()[:-1]

def nomb():
    f = open("phrasescor.txt","r")
    ch = f.readline()[:-1]
    n = 0
    m = 0
    while ch !="":
        for i in range(len(ch)):
            if ch[i] == " ":
                n += 1 
        m += 1
        ch = f.readline()[:-1]
    w.nombre.addItem("Le nombres de mots = "+str(n+m)+"\nLe nombre des phrases = "+str(m) +"\nLa moyenne de mots par phrase "+str((m+n)/m) )




app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.enregistrer.clicked.connect(enr)
w.affcor.clicked.connect(corig)
w.affnb.clicked.connect(nomb)
app.exec_()