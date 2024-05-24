from PyQt5.uic import * 
from PyQt5.QtWidgets import *
from random import randint
from numpy import array

def dess(): 
    n = w.textn.text()
    if not(n != "" and n.isdecimal() and 4<int(n)<20):
        QMessageBox.critical(w,"erruer","n non valide")
    else : 
        n = int(n)
        m = array([[int]*n]*n)
        w.table.setColumnCount(n)
        w.table.setRowCount(n)
        for i in range(n):
            for j in range(n):
                ent = randint(2,99)
                m[i,j] = ent
                w.table.setItem(i,j,QTableWidgetItem(str(ent)))
        
def tril(i,n):
    test = True
    for j in range(n-1):
        if not(int(w.table.item(i,j+1).text()) >= int(w.table.item(i,j).text())) :
            test = False
    test1 = True
    for j in range(1,n):
        if not(int(w.table.item(i,j-1).text()) >= int(w.table.item(i,j).text())):
            test1 = False
    return test or test1
def tric(i,n):
    test = True
    for j in range(n-1):
        if not(int(w.table.item(j+1,i).text()) >= int(w.table.item(j,i).text())) :
            test = False
    test1 = True
    for j in range(1,n):
        if not(int(w.table.item(j-1,i).text()) >= int(w.table.item(j,i).text())):
            test1 = False
    return test or test1

def remp():
    w.list.clear()
    f = open("resultat.txt","w")
    n = w.table.rowCount()
    ch1 = ""
    for i in range(n): 
        if tril(i,n):
            ch1 += "\nL"+str(i+1)+"*"
            for j in range(n):
                ch1 += w.table.item(i,j).text() + "-"
            ch1 = ch1[:-1]
        if tric(i,n):
            ch1 += "\nC"+str(i+1)+"*"
            for j in range(n):
                ch1 += w.table.item(j,i).text() + "-"
            ch1 = ch1[:-1]
    w.list.addItem(ch1)


app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.dessiner.clicked.connect(dess)
w.remplir.clicked.connect(remp)
app.exec_()