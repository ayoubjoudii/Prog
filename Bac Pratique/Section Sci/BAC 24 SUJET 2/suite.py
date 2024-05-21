from PyQt5.uic import *
from PyQt5.QtWidgets import * 

def trier(ch):
    perm = True 
    while perm :
        perm = False
        for k in range(0,len(ch)-2,2):
            bloc1 = ch[k:k+2]
            bloc2 = ch[k+2:k+4]
            if bloc1 > bloc2 : 
                ch = ch[0:k] + bloc2 + bloc1 + ch[k+4:len(ch)]
                perm = True
    return ch

def calculer(x):
    n = int(x[2:4]) - int(x[0:2]) 
    i = 4
    while i<len(x)-3 and n!= 0:
        if (int(x[i+2:i+4]) - int(x[i:i+2]) != n):
            n = 0
        else : 
            n = int(x[i+2:i+4] ) -int(x[i:i+2]) 
        i = i+2
    return n  

def play():
    x = w.textx.text()
    if x=="" or x.isnumeric()==False or len(x)<6 or len(x)>20 or len(x)%2 != 0:
        w.res.setText("verifier donnes")
    else: 
        x = trier(x)
        r = calculer(x)
        if r == 0:
            w.res.setText("Les tranches de chiffres triees "+x+"ne forment pas des termes\n dune suite arithmetique")
        else : 
            w.res.setText("Les tranches de chiffres triees "+x+" forment des termes\n dune suite arithmetique (r="+str(r)+")")



app = QApplication([])
w = loadUi("interfacearithmetique.ui")
w.show()
w.verifier.clicked.connect(play)
app.exec_()