from PyQt5.uic import *
from PyQt5.QtWidgets import *
from pickle import dump,load
from math import * 


def f(x):
    return x*sin(x)*sin(x)

def pointfixe():
    x = 1
    while abs(x-f(x)) > 0.001:
        x = f(x)
    return f(x)
def trapeze(a,b,n):
    h = (b-a)/n
    s= 0
    x = a
    for i in range(n):
        s += (f(h+x)+f(x))/2 
        x += h 
    return s*h 
def rectangle(a,b,n):
    h = (b-a)/n
    s= 0
    x = a
    for i in range(n):
        s += f(x) 
        x += h 
    return s*h 
def calcair():
    f = open("aire.fch","wb")
    f
    a = pi/2
    b = pi
    l = 0
    for i in range(5,106,5):
        tr = trapeze(a,b,i)
        rec = rectangle(a,b,i)
        w.table.insertRow(l)
        w.table.setItem(l,0,QTableWidgetItem(str(i)))
        w.table.setItem(l,1,QTableWidgetItem(str(tr)))
        w.table.setItem(l,2,QTableWidgetItem(str(rec)))
        l += 1
        e = dict(air)
        e["nb"] = i
        e["trap"] = tr
        e["rect"] = rec
        dump(e,f)
    f.close()

def traiter():
    pf = w.pf.isChecked()
    ai = w.ai.isChecked()
    tous = w.tous.isChecked()
    if tous or (pf and ai) or (pf and ai and tous) :
        f = open("resultat.txt","w")
        l1 = "x*sin(x)*sin(x)\nLe point fixe = "+str(pointfixe())+"\nn         Trapeze         Rectangle\n"
        fb = open("aire.fch","rb")
        calcair()
        w.table.setRowCount(0)
        test = True 
        while test:
            try : 
                x = load(fb)
                l1 += str(x["nb"]) + "         "+str(x["trap"]) + "         "+str(x["rect"]) +"\n"
            except:
                test = False 
        f.write(l1)
        w.list.addItem(l1)
    elif pf :
        w.table.setRowCount(0)
        w.res.setText(str(pointfixe()))
    elif ai: 
        w.table.setRowCount(0)
        w.res.clear()
        calcair()
    else:
        QMessageBox.critical(w,"erreur","choisit une chose")




air = {
    "nb" : int,
    "trap" : float,
    "rectangle" : float
}
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.calc.clicked.connect(traiter)
app.exec_()