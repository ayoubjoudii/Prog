from PyQt5.uic import * 
from PyQt5.QtWidgets import * 
from pickle import dump,load


def reel(n):
    test = True 
    try : 
        test = 0.001<=float(n)<= 0.1
    except : 
        test = False
    return test 
def f(x):
    return x*x
def rectangle(a,b,n):
    h = (b-a)/n
    x = a
    s = f(x)
    for i in range(n):
        x = x+h
        s = s+f(x)
    return s*h
def trapeze(a,b,n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range(n):
        s = s+(f(x+h)+f(x))/2
        x = x + h
    return s * h

def play():
    ep = w.ep.text()
    f = open("air.dat","wb")
    if ep == "" or reel(ep) == False :
        QMessageBox.critical(w,"erreur","epsilon entre 0.001 and 0.1")
    else : 
        ep = float(ep)
        r = rectangle(0,3,1)
        t = trapeze(0,3,1)
        n = 0
        w.table1.setRowCount(0)
        w.list.clear()
        while abs(r-9) > ep and abs(t-9) > ep:
            w.table1.insertRow(n)
            w.table1.setItem(n,0,QTableWidgetItem(str(n+1)))
            w.table1.setItem(n,1,QTableWidgetItem(str(r)))
            w.table1.setItem(n,2,QTableWidgetItem(str(t)))
            n += 1
            e = dict(div)
            e["n"] = n
            e["rect"] = r
            e["trap"] = t
            dump(e,f)
            r = rectangle(0,3,n)
            t = trapeze(0,3,n)
        if abs(9-t) <= ep : 
            w.list.addItem("Methode plus proche = methode de trapezes \n valeur approchee = "+str(t)+"\nNombres de divisions = "+str(n))
        elif abs(9-r) <= ep:
            w.list.addItem("Methode plus proche = methode de rectangles \n valeur approchee = "+str(t)+"\nNombres de divisions = "+str(n))



            


div = {
    "n": int,
    "rect" : float,
    "trap" : float
}
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.calc.clicked.connect(play)
app.exec_()