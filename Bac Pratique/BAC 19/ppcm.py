from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load
from numpy import array 

def puis(a, b):
    if b == 0:
        return 1
    else:
        return a * puis(a, b - 1)


def ppcm(a, b):
    t1 = array([eng]*10)
    t2 = array([eng]*10)
    p = 2
    i = 0
    while a > 1:
        if a % p ==0 :
            nb = 0
            while a % p == 0:
                a = a // p
                nb += 1
            t1[i] = dict(eng)
            t1[i]["n"] = p
            t1[i]["p"] = nb
            i += 1
        else:
            p+= 1 
    
    
    p2 = 2
    i2 = 0
    while b > 1:
        if b % p2 ==0 :
            nb = 0
            while b % p2 == 0:
                b = b // p2
                nb += 1
            t2[i2] = dict(eng)
            t2[i2]["n"] = p2
            t2[i2]["p"] = nb
            i2 += 1
        else:
            p2+= 1 
    
    
    
    s = 1
    for f in range(i):
        prime1 = t1[f]["n"]
        power1 = t1[f]["p"]
        primein2 = False
        for g in range(i2):
            if t2[g]["n"] == prime1:
                primein2 = True
                powerin2 = t2[g]["p"]
        if primein2:
            if power1 > powerin2 :
                s *= puis(prime1, power1) 
            else:
                s *= puis(prime1, powerin2) 
        else:
            s *= puis(prime1, power1)

    for f in range(i2):
        prime2 = t2[f]["n"]
        power2 = t2[f]["p"]
        primein1 = False
        for g in range(i):
            if t1[g]["n"] == prime2:
                primein1 = True
        if not primein1:
            s *= puis(prime2, power2)
    return s
        

def ajouter():
    a = w.na.text()
    b = w.nb.text()
    if not (a.isnumeric()) or int(a)<=0 or int(a)>=1000:
        QMessageBox.critical(w,"erreur","a entier positif")
    elif not (b.isnumeric()) or int(b)<=0 or int(b)>=1000:
        QMessageBox.critical(w,"erreur","b entier positif")
    else: 
        f = open("ppcm.dat","ab")
        e = dict(pp)
        e["a"] = int(a)
        e["b"] = int(b)
        e["ppcm"] = ppcm(int(a),int(b))
        dump(e,f)
        f.close()
def afficher():
    f = open("ppcm.dat","rb")
    end = True 
    i = 0
    w.table.setRowCount(0)
    while end : 
        try: 
            x = load(f)
            w.table.insertRow(i)
            w.table.setItem(i,0,QTableWidgetItem(str(x["a"])))
            w.table.setItem(i,1,QTableWidgetItem(str(x["b"])))
            w.table.setItem(i,2,QTableWidgetItem(str(x["ppcm"])))
            i += 1
        except: 
            end = False
    
eng = {
    "n" : int,
    "p" : int
}
pp = {
    "a" : int,
    "b" : int,
    "ppcm" : int
}
app = QApplication([])
w = loadUi("ppcm.ui")
w.show()
w.ajouter.clicked.connect(ajouter)
w.afficher.clicked.connect(afficher)
app.exec_()