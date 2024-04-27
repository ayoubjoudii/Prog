from PyQt5.uic import *
from PyQt5.QtWidgets import *
from pickle import dump,load

def big(x):
    x = int(x)
    p  = 1
    while p*p < x:
        p = p +1
    return p 
def approch(x , p):
    x = int(x)
    ep = 0.00005
    up = p 
    u = (1/2)*(up + x / up)
    while abs(u - up) <= ep :
        up = u
        u = (1/2)*(up + x / up)
    return u 
        
def racine():
    ch = w.valeur.text()
    if ch=="" :
        QMessageBox.critical(w,"erreur","yaweldi feere8")
    elif not (2<=int(ch)<=200) :
        QMessageBox.critical(w,"erreur","yaweldi positive")
    else: 
        f=open("aprochee.dat","ab")
        e = dict(rac)
        e["x"] = float(ch)
        e["RC"] = approch(ch,big(ch))
        dump(e,f)
        

def afficher():
    f = open("aprochee.dat","rb")
    test = True
    i = 0
    w.table.setRowCount(0)
    while test: 
        try : 
            x = load(f)
            w.table.insertRow(i)
            print(x["RC"],x["x"])
            w.table.setItem(i,0,QTableWidgetItem(str(x["x"])))
            w.table.setItem(i,1,QTableWidgetItem(str(x["RC"])))
            i = i +1
        except : 
            test = False
    

rac = {
    "x" : float,
    "RC" : float 
}
app = QApplication([])
w = loadUi("interface_racine.ui")
w.show()
w.ajouter.clicked.connect(racine)
w.afficher.clicked.connect(afficher)
app.exec_()