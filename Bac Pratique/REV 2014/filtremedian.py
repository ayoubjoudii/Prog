from PyQt5.uic import * 
from PyQt5.QtWidgets import * 
from numpy import array
from pickle import dump,load

def conv(ch):
    ch = ch[:-1]
    p = 1
    n = 0
    for i in range(len(ch)-1,-1,-1):
        n += int(ch[i]) *p 
        p *= 2
    return n
def dimension():
    haut = w.haut.text()
    larg = w.larg.text()
    if haut + larg == "" or not(haut.isdecimal() and larg.isdecimal() and 5<=int(haut)<=10 and 5<=int(larg)<=10 ) :
        QMessageBox.critical(w,"erreur","verifier hauteur et largeur entre 5 et 10")
    else: 
        f = open("imageinit.txt","w")
        f.write(haut+"x"+larg+"\n")


def ajout():
    pixel = w.pixel.text()
    test = (len(pixel) == 8)
    for i in range(len(pixel)):
        if pixel[i] != "1" and pixel[i] != "0":
            test = False 
    if test == False:
        QMessageBox.critical(w,"erreur","verifier pixel 8 bits")
    else : 
        f = open("imageinit.txt","a")
        f.write(pixel+"\n")
def vois(d,f,m,i,j):
    t = array([int]*(f-d)*(f-d))
    l = 0
    for v in range(i+d,i+f):
        for b in range(j+d,j+f):
            try : 
                if v < 0 or b < 0 :
                    t[l] = 0
                else : 
                    t[l] = m[v,b]
            except: 
                t[l] = 0
            l += 1
    perm = True
    while perm:
        perm = False
        for i in range(l-1):
            if t[i] > t[i+1]:
                temp = t[i]
                t[i] = t[i+1]
                t[i+1] = temp
                perm = True
    median = t[l//2]
    return median 


def filtre():
    filt = w.filtre.currentText()
    f = open("imageinit.txt","r")
    fb = open("imageinit.dat","wb")
    ch = f.readline()
    h = int(ch[:ch.find("x")])
    l = int(ch[ch.find("x")+1:]) 
    m = array([[int]*l]*h)
    mf = array([[int]*l]*h)
    for i in range(h):
        for j in range(l):
            m[i][j] = conv(f.readline())
    n = int(filt[0])
    for i in range(h):
        for j in range(l):
            if n == 3:
                median = vois(-1,2,m,i,j)
            elif n == 5:
                median = vois(-2,3,m,i,j)
            elif n == 7:
                median = vois(-3,4,m,i,j)
            mf[i,j] = median 
            e = dict(mff)
            e["numl"] = i
            e["numc"] = j
            e["val"] = median
            dump(e,fb)
                


def affo():
    f = open("imageinit.txt","r")
    ch = f.readline()
    i = 0
    w.tableo.setRowCount(0)
    while ch != "":
            w.tableo.insertRow(i)
            w.tableo.setItem(i,0,QTableWidgetItem(ch[:-1]))
            ch = f.readline()
            i += 1
    f.close()

def afff():
    f = open("imageinit.dat","rb")
    test = True
    i = 0
    w.tablef.setRowCount(0)
    while test :
        try : 
            x = load(f)
            w.tablef.insertRow(i)
            w.tablef.setItem(i,0,QTableWidgetItem(str(x["numl"])))
            w.tablef.setItem(i,1,QTableWidgetItem(str(x["numc"])))
            w.tablef.setItem(i,2,QTableWidgetItem(str(x["val"])))
            i += 1
        except:
            test = False 
    f.close()

mff = {
    "numl" : int,
    "numc" : int,
    "val" : int
}
app = QApplication([])
w = loadUi("interfacefiltre.ui")
w.show()
w.dimension.clicked.connect(dimension)
w.ajoutp.clicked.connect(ajout)
w.filtrer.clicked.connect(filtre)
w.afficho.clicked.connect(affo)
w.affichf.clicked.connect(afff)
app.exec_()