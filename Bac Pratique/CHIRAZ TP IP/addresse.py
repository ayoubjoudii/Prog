from PyQt5.uic import * 
from PyQt5.QtWidgets import * 
from pickle import dump,load 

def valid(ch):
    n = 0 
    for i in range(len(ch)):
        if ch[i] == ".":
            n += 1
    test = n == 3 
    while ch.find(".") != -1:
        p = ch.find(".")
        if not(ch[:p].isdecimal() and 0<=int(ch[:p])<=255):
            test = False
        ch = ch[p+1:]
    return test and ch.isdecimal() and 0<=int(ch)<=255    
def ajout():
    ip = w.ip.text()
    if ip == "":
        QMessageBox.critical(w,"erreur",'addrese fergha')
    elif not valid(ip):
        QMessageBox.critical(w,"erreur",'addresse ip non valide')
    else : 
        f = open("addresse4.txt","a")
        f.write(ip+"\n")
        QMessageBox.information(w,"succes","ajoutéé")

def afftxt():
    f = open("addresse4.txt","r")
    w.list.clear()
    ch = f.read()
    w.list.addItem(ch)
def conv(n):
    n = int(n)  
    ch = ""
    while n != 0:
        r = n%2
        n //= 2
        ch = str(r) + ch
    return ch
def classe(ch):
    p = ch.find(".")
    cl = conv(ch[:p])
    if cl[0] == "0":
        return "A"
    elif cl[:2] == "10":
        return "B"
    elif cl[:3] == "110":
        return "C"
    elif cl[:4] == "1110":
        return "D"
    elif cl[:5] == "1111":
        return "E"
def hexa(n):
    n = int(n)
    ch = ""
    while n != 0:
        r = n%16
        n = n//16
        if r>9 : 
            ch = chr(r+55) + ch
        else : 
            ch = str(r) + ch
    return ch 
def ipv6(ch):
    res = ""
    for i in range(2):
        p = ch.find(".")
        res += hexa(ch[:p])
        ch = ch[p+1:]
    res += ":"
    p = ch.find(".")
    res += hexa(ch[:p]) + hexa(ch[p+1:])
    return res



def generer():
    f = open("addresse4.txt","r")
    fb = open("addresse6.dat","wb")
    ch = f.readline()[:-1]
    while ch != "":
        e = dict(ip)
        e["ipv4"] = ch
        cl = classe(ch)
        e["classe"] = cl
        e["ipv6"] = ipv6(ch)
        dump(e,fb)
        ch = f.readline()[:-1]
    f.close()

def afficher():
    f = open("addresse6.dat","rb")
    cl = w.type.currentIndex()
    clt = w.type.currentText()
    check = w.ipv4.isChecked()
    if cl == 0 :
        QMessageBox.warning(w,'erreur',"choisit une chose ")
    elif check : 
        afftxt()
    else : 
        test = True 
        w.table.setRowCount(0)
        i = 0
        if cl == 1 : 
            while test : 
                try : 
                    x = load(f)
                    w.table.insertRow(i)
                    w.table.setItem(i,0,QTableWidgetItem(x["ipv4"]) )
                    w.table.setItem(i,1,QTableWidgetItem(x["classe"]) )
                    w.table.setItem(i,2,QTableWidgetItem(x["ipv6"]) )
                    i +=1
                except:
                    test = False 
        else : 
            while test : 
                try : 
                    x = load(f)
                    if x["class"] == clt[:-1] : 
                        w.table.insertRow(i)
                        w.table.setItem(i,0,QTableWidgetItem(x["ipv4"]) )
                        w.table.setItem(i,1,QTableWidgetItem(x["class"]) )
                        w.table.setItem(i,2,QTableWidgetItem(x["ipv6"]) )
                        i +=1
                except:
                    test = False 
            
    f.close()


ip = {
    "ipv4" : str,
    "class" : str,
    "ipv6" : str
}
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.afficher.clicked.connect(afficher)
w.ajout.clicked.connect(ajout)
w.former.clicked.connect(generer)
app.exec_()
