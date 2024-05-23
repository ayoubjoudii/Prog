from PyQt5.uic import *
from PyQt5.QtWidgets import *
from pickle import dump,load


def somme(x):
    x = str(x)
    s = 0
    for i in range(len(x)):
        s = s + int(x[i])
    return s

def rigolo(n):
    s1 = somme(n)
    s2 = 0 
    i = 2
    while n != 1 :
        if n % i == 0:
            s2 += somme(i) 
            n = n // i
        else : 
            i += 1
    return s1 == s2
    
def facteur(x):
    ch = ""
    i = 2
    while x != 1 :
        if x % i == 0:
            ch += str(i) + "," 
            x = x // i
        else : 
            i += 1
    return ch[:-1]

def aff():
    a = w.texta.text()
    b = w.textb.text()
    if not(a != "" and b != "" and a.isnumeric() and b.isnumeric() and 100<int(a) and int(b)<1000 and int(a)<int(b)):
        QMessageBox.critical(w,"erreur","verifier a et b ")
    else : 
        w.list.clear()
        f = open("rigolo.dat","wb")
        for i in range(int(a),int(b)+1):
            if rigolo(i):
                w.list.addItem(str(i)+"\n")
                e = dict(rigoloo)
                e["n"] = i
                e["fact"] = facteur(i)
                dump(e,f)    
        f.close() 
            
def lister():
    if w.lister.isChecked() : 
        f = open("rigolo.dat","rb")
        test = True 
        i = 0 
        w.table.setRowCount(0)
        while test : 
            try : 
                x = load(f)
                w.table.insertRow(i)
                w.table.setItem(i,0,QTableWidgetItem(str(x["n"])))
                w.table.setItem(i,1,QTableWidgetItem(x["fact"]))
                i += 1
            except : 
                test = False
        f.close()
    else : 
        w.table.setRowCount(0)
                


def annuler():
    w.texta.setText("")
    w.textb.setText("")
    w.table.setRowCount(0)
    w.list.clear()

rigoloo = {
    "n" : int,
    "fact" : str
}
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.afficher.clicked.connect(aff)
w.annuler.clicked.connect(annuler)
w.lister.clicked.connect(lister)
app.exec_()
