from PyQt5.uic import *
from PyQt5.QtWidgets import *
from numpy import array 

def deconv(i):
    ch = ""
    for j in range(8):
        ch += m[i][j]
    s = 0
    p = 1
    for i in range(len(ch)-1,-1,-1):
        s += int(ch[i]) * p
        p*= 2
    print(ch,str(s))
    return str(s)
     
def conv2(n):
    ch = ""
    while n != 0:
        r = n%2
        n //= 2
        ch = str(r)+ch
    while len(ch)<8:
        ch = "0"+ch
    return ch
def remplir(i,m,ch):
    w.table.setColumnCount(8)
    w.table.insertRow(i)
    for j in range(8):
        m[i][j] = ch[j]
        w.table.setItem(i,j,QTableWidgetItem(ch[j]))

def conv():
    global siz
    f = open("message.txt","a")
    ch = w.origin.toPlainText()
    if not(0<=len(ch)<=20):
        QMessageBox.critical(w,"errreur","entrer un message entre 0 et 20")
    else: 
        f.write(ch+"\n")
        for siz in range(len(ch)):
            remplir(siz,m,conv2(ord(ch[siz])))
        QMessageBox.information(w,"success","Conv success")
def inv():
    for i in range(siz):
        for j in range(8):
            if m[i][j] == "0":
                w.table.setItem(i,j,QTableWidgetItem("1"))
                m[i][j] = "1"
            else:
                w.table.setItem(i,j,QTableWidgetItem("0"))
                m[i][j] = "0"
    QMessageBox.information(w,"success","inverseees ")
def crypter():
    ch = ""
    f = open("crypte.txt","a")
    for i in range(siz):
        ch += deconv(i) + "*"
    w.list.addItem(ch)
    f.write(ch[:-1]+"\n")
    QMessageBox.information(w,"success","cryptes")




def initt():
    w.table.setRowCount(0)
    w.table.setColumnCount(0)
    w.origin.setText("")
    w.list.clear()


m = array([[str]*8]*20)
app = QApplication([])
w = loadUi("crypt.ui")
w.show()
w.conv.clicked.connect(conv)
w.inverser.clicked.connect(inv)
w.crypter.clicked.connect(crypter)
w.init.clicked.connect(initt)
app.exec_()