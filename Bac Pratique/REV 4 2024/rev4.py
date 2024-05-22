from PyQt5.uic import * 
from PyQt5.QtWidgets import * 
from pickle import dump,load


def pgcd(a,b):
    if a==b:
        return a
    if a>b:
        return pgcd(a-b,b)
    if a<b : 
        return pgcd(a,b-a)
def former(n):
    f = open("div.dat","wb")
    fb = open("resultat.txt","w")    
    p = 0
    ch = ""
    for i in range(1,n):
        if n % i == 0:
            e = dict(parf)
            e["nb1"] = i
            e["nb2"] = n//i
            if pgcd(i , n//i) == 1:
                e["prim"] = "oui"
                p = p+i
                ch = ch + str(i) +"+"
            else : 
                e["prim"] = "non"
            dump(e,f)
    if p == n:
        fb.write("n = "+str(n)+" est unitairemetn parfait car "+ch[:-1]+"="+str(n))
    else: 
        fb.write("n = "+str(n)+" n est pas unitairemetn parfait car "+ch[:-1]+"!="+str(n))
    f.close()
    fb.close()
def remp():
    n = w.textn.text()
    former(int(n))
    fb = open("div.dat","rb")
    test = True
    i=0
    w.table.setRowCount(0)
    while test : 
        try :
            x = load(fb)
            w.table.insertRow(i)
            w.table.setItem(i,0 , QTableWidgetItem(str(x["nb1"])) )
            w.table.setItem(i,1 , QTableWidgetItem(str(x["nb2"])) )
            w.table.setItem(i,2 , QTableWidgetItem(x["prim"]) )
            i += 1
        except: 
            test = False
    fb.close()

def resultat():
    f = open("resultat.txt","r")
    ch = f.read()
    w.clear()
    w.list.addItem(ch)
    f.close()



parf = {
    "nb1" : int,
    "nb2" : int,
    "prim" : str
}
app = QApplication([])
w = loadUi("parfait.ui")
w.show()
w.rempaff.clicked.connect(remp)
w.resultat.clicked.connect(resultat)
app.exec_()