from PyQt5.uic import *
from PyQt5.QtWidgets import * 
from random import randint
from pickle import load,dump

def ajouter():
    def verif(ch):
        test = True 
        for i in range(0,len(ch)):
            if not("A"<=ch[i]<="Z" or ch[i] == " ") :
                test = False
        return test  
    ch =  w.text.text()
    f = open("msg.txt","a")
    if ch == "": 
        QMessageBox.critical(w,'ereur',"le message est une chaine vide") 
    elif not(verif(ch)) :
        QMessageBox.critical(w,'ereur',"le message doit majuscules et espaces") 
    else : 
        f.write(ch+"\n")
    
def affich():
    f = open("msg.txt",'r')
    ch = f.readline()
    w.msg.clear()
    while ch != "":
        w.msg.addItem(ch)
        ch = f.readline()
def creer():
    def espace(ch):
        ch1 = ""
        if ch.find(" ") == -1 :
            ch1 = ""
        else : 
            for i in range(0,len(ch)):  
                if ch[i] == " ":
                    ch1 = ch1 + str(i) + "*"
            ch1 = ch1[:-1]
        return ch1
    def effacer(ch):
        lettre = "AZERTYUIOPQSDFGHJKLMWXCVBN"
        i = 0
        while i<len(ch):
            if ch[i] == " ":
                ch  = ch[0:i] + ch[i+1:]
            i = i+1
        ch = ch[:-1]
        while len(ch)%3 != 0:
            ch = ch+lettre[randint(0,len(lettre)-1)]
        return ch
    def triplet(ch):
        k = 0
        s = 1
        ch4 = ""
        for i in range(0,len(ch)):
            k = k +1
            s = s* ord(ch[i])
            if k == 3:
                s1 = 0
                for i in range(0,len(str(s))):
                    s1 = s1 + int(str(s)[i])
                while s1 > 9 :
                    c = str(s1)
                    s1 = 0
                    for i in range(0,len(c)):
                        s1 = s1 + int(c[i])
                    ch4 = ch4 + str(s1)
                k = 0
                s = 1
        return ch4
    f = open("msg.txt",'r')
    ch = f.readline()
    i = 0
    fb = open("codes.dat","ab")
    while ch != "":
        e = dict(code)
        ch1 = espace(ch)
        e["msg1"] = ch1
        ch = effacer(ch)
        ch2 = triplet(ch)
        e["msg2"] = ch2
        dump(e,fb)
        w.table.insertRow(i)
        w.table.setItem(i , 0 ,QTableWidgetItem(ch1))
        w.table.setItem(i , 1 ,QTableWidgetItem(ch2))
        ch = f.readline()
        i = i +1    

     
code = {
    "msg1" : str,
    "msg2" : str
}
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.ajouter.clicked.connect(ajouter)
w.afficher.clicked.connect(affich)
w.coder.clicked.connect(creer)
app.exec_()