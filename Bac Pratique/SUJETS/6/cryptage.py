from PyQt5.uic import * 
from PyQt5.QtWidgets import *
from random import randint
from pickle import dump,load


def generer():
    ch = w.mess.toPlainText()
    if not valid(ch):
        QMessageBox.critical(w,"erreur","seulement des espaces!!")
    else : 
        cle = ""
        for i in range(len(ch)):
            cle += randint(0,9) 
def enr():
    
def crypter():

def afficher():


app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.cle.clicked.connect(generer)
w.enregistrer.clicked.connect(enr)
w.crypt.clicked.connect(crypter)
w.aff.clicked.connect(afficher)
app.exec_()