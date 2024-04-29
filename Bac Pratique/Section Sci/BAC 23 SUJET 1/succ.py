from PyQt5.QtWidgets import *
from PyQt5.uic import *

def verif(m,n):
    ch = m + n
    ch1 = ""
    while ch != "" :  
        temp = ch[0]
        p = 0
        for i in range(1,len(ch)):
            if ch[i] > temp :
                temp = ch[i]
                p = i
        ch1 = temp + ch1 
        ch = ch[:p]+ch[p+1:] 
    test = True
    for i in range(len(ch1)-1):
        if int(ch1[i])+1 != int(ch1[i+1]):
            test = False 
    return test

def play():
    m = w.valuem.text()
    n = w.valuen.text()
    if not(m.isnumeric() and int(m) >= 0 ):
        QMessageBox.critical(w,"erreur","m positif entier")
        w.resultat.setText("m positif entier")
    elif not(n.isnumeric() and int(n) >= 0 ):
        QMessageBox.critical(w,"erreur","n positif entier")
        w.resultat.setText("n positif entier")
    else : 
        if verif(m,n):
            w.resultat.setText("m et n forment une succesion parfaite")
        else : 
            w.resultat.setText("m et n ne forment pas une succesion parfaite")


app = QApplication([])
w = loadUi("interfacesuccession.ui")
w.show()
w.verifier.clicked.connect(play)
app.exec_()