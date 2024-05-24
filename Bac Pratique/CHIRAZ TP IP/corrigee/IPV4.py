from PyQt5.uic import*
from PyQt5.QtWidgets import *
from pickle import load,dump




def ajouter():
    ch=w.l1.text()
    if ch=="":
        QMessageBox.critical(w,"erreur","on peut pas ajouter une adresse vide!!")
    elif ch[0]=="." or ch[len(ch)-1]=="." or valid(ch)==False or recherche(ch)==True :
        QMessageBox.critical(w,"erreur","ip non valide!!")
    else :
        f=open("IPV4.txt","a")
        f.write(ch+"\n")
        QMessageBox.information(w,"info","adresse IP ajoutee avec succés!")
        f.close()
        


def valid(ch):
    np=0
    test=True
    for i in range(len(ch)):
        if ch[i]==".":
            np= np + 1
    d=ch.find("..")
    if np!=3  or d!=-1:
        test=False
    ch = ch+"."
    while test and ch!="":
        ch2=ch[0:ch.find(".")]
        if ch2.isdecimal()== False or  not(0<=int(ch2)<=255) :
            test=False
        ch=ch[ch.find(".")+1:]

    return test
    

def recherche(ch):
    f=open("IPV4.txt","r")
    chf=f.read()
    f.close()
    return chf.find(ch)!=-1

def afficher():
    if w.c1.currentIndex()==0 :
        QMessageBox.warning(w,"python","Il faut choisir un type d'affichage")
    elif w.ch1.isChecked() :
        f=open("IPV4.txt","r")
        chf=f.read()
        w.list.addItem(chf)
        f.close()
    elif w.c1.currentIndex()==1 :
        affichefich()
    else :
        affchoix(w.c.currentIndex())

def affichefich():
    w.table.setRowCount(0)
    f1=open("IPV6.dat","rb")
    test=True
    i=0
    while test :
        try:
            e=load(f1)
            w.table.insertRow(i)
            w.table.setItem(i,0,QTableWidgetItem(e["IPV4"]))
            w.table.setItem(i,1,QTableWidgetItem(e["classe"]))
            w.table.setItem(i,2,QTableWidgetItem(e["IPV6"]))
            i+=1
        except :
            test=False 
    f1.close()       
    
def affchoix(x):
    w.table.setRowCount(0)
    f1=open("IPV6.dat","rb")
    test=True
    i=0
    while test :
        try:
            e=load(f1)
            
            if e["classe"]== chr(64+x) :
                w.table.insertRow(i)
                w.table.setItem(0,i,QTableWidgetItem(e["IPV4"]))
                w.table.setItem(1,i,QTableWidgetItem(e["classe"]))
                w.table.setItem(2,i,QTableWidgetItem(e["IPV6"]))
                i+=1
            
        except :
            test=False 
    f1.close() 
    
def conv(x,b):
    chx="0123456789ABCDEF"
    ch=""
    while x!=0 :
        r=x%b
        ch=chx[r]+ch
        x//=b
    return ch
        
def binaire(x):
    chb=conv(x,2)
    while len(chb)<8:
        chb="0"+chb
    return chb
    


def former():
    f=open("IPV4.txt","r")
    f1=open("IPV6.dat","wb")
    ch=f.readline()[:-1]
    while ch!="" :
        e=dict(rac)
        binn=binaire(int(ch[0:ch.find(".")]))
        if binn[0] == "0" :
            e["classe"]="A"
        elif binn[0:2]=="10" :
            e["classe"]="B"
        elif binn[0:3]=="110" :
            e["classe"]="C"
        elif binn[0:4]=="1110" :
            e["classe"]="D"
        elif binn[0:4]=="1111" :
            e["classe"]="E"
        e["IPV4"]=ch   
        e["IPV6"]= generer (ch+".")
        dump(e,f1)
        ch=f.readline()[:-1]
    f.close()
    f1.close()
            
        
        
def generer(ch):
    i=1
    gen=""
    while ch!="":
        ch2=ch[:ch.find(".")]
        if i==2 :
            gen = gen+ conv(int(ch2),16) +":"
        else :
            gen = gen+ conv(int(ch2),16)
        i=i+1
        ch=ch[ch.find(".")+1:]
    return gen
    
    
    
    




rac ={"IPV4" :str , "classe" : str , "IPV6":str}
app= QApplication([])
f=open("IPV4.txt","a")
f.close()
w = loadUi("IP.ui")
w.show()
w.b1.clicked.connect(ajouter)
w.b2.clicked.connect(former)
w.b3.clicked.connect(afficher)
app.exec_()
