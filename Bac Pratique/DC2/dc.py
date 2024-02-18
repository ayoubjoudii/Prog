from PyQt5.uic import *
from PyQt5.QtWidgets import *
from pickle import dump,load 
def generer():
    c = w.client.text()
    n = w.nom.text()
    p = w.prenom.text()
    def alpha (ch):
        if len(ch) < 4 :
            return False 
        for i in range(len(ch)):
            if not("A"<=ch[i]<="Z") :
                return False
        return True 
    def mod(n , p ):
        ch = n[:4] + p[:4]
        m = ""
        def conv(x,b):
            c = ""
            xr = "0123456789ABCDEF"
            while x != 0:
                r = x%b
                x = x//b
                c = xr[r] + c
            return c
        def pgcd(n):
            def prime(x):
                l = 0
                for i in range(2, x//2+1):
                    if x % i == 0:
                        l = l+1
                return l == 0
            i = n - 1
            while i >= 0 :
                i = i - 1
                if n%i == 0 and prime(i):
                    return i
        for i in range(len(ch)):
            if "A"<=ch[i]<="F" : 
                m = m + chr(64 + int(conv(ord(ch[i])-55,8))) 
            elif "G"<=ch[i]<="I":
                m = m + str(ord(ch[i])-64)
            else: 
                d = pgcd(ord(ch[i]))
                m = m + conv(d,16)

        return m
    if len(c) != 8 or not c.isdigit() :
        QMessageBox.critical(w,"code","code 8 chiffres!")
    elif not alpha(n) :
        QMessageBox.critical(w,"nom","lettres majuscule 4!")
    elif not alpha(p):
        QMessageBox.critical(w,"prenom","lettres majuscule 4!")
    else: 
        d = dict(client)
        if w.eparn.isChecked() : 
            compte = "epargne"
        elif w.courant.isChecked():
            compte = "courant"
        md = mod(n,p)
        d["cnt"] = compte
        d["c"] = c
        d["n"] = n
        d["p"] = p
        d["mdp"] = md
        f = open("mdpass.dat","ab")
        dump(d,f)
        f.close()
def afficher():
    def div(n):
        ch = "132"
        n = str(n)
        while len(n) > 1:
            i = len(n)
            sig = 1
            k = 0
            x = 0
            while i > 0 :
                i = i-1
                x = x + int(n[i])*(int(ch[k])*sig)
                k = k +1 
                if k == 3: 
                    sig = -sig
                    k = 0
            n = str(x)
        return n == "0" or n == "7"
    w.list.addItem("le code divisble par 7 :")
    fb = open("mdpass.dat","rb")
    fin = True
    i = 0
    while fin:
        try: 
            x = load(fb)
            w.table.insertRow(i)
            w.table.setItem(i,0,QTableWidgetItem(x["c"]))
            w.table.setItem(i,1,QTableWidgetItem(x["n"]))
            w.table.setItem(i,2,QTableWidgetItem(x["p"]))
            w.table.setItem(i,3,QTableWidgetItem(x["cnt"]))
            w.table.setItem(i,4,QTableWidgetItem(x["mdp"]))
            if div(x["c"][0]) : 
                w.list.addItem(x["n"]+" "+x["p"])
            i = i +1
        except:
            fin = False 


client = {
    "c" : int,
    "n" : str,
    "p" : str,
    "cnt" : str,
    "mdp" : str
}
app = QApplication([])
w = loadUi("dc.ui")
w.show()
w.mdp.clicked.connect(generer)
w.afficher.clicked.connect(afficher)
app.exec_()