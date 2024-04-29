from PyQt5.QtWidgets import * 
from PyQt5.uic import * 
from pickle import load,dump 

def verif(ch):
    for i in range(0,len(ch)):
        if not("A"<=ch[i].upper()<="Z" or ch[i].isdecimal() or ch==""):
            return False
    return True
def verif1(n ):
    for i in range(0,len(n)):
        if not("0"<=n[i]<="9"):
            return False
    return True
def ajouter():
    id = w.id.text()
    tel = w.tel.text()
    male = w.male.isChecked()
    female = w.female.isChecked()
    ville = w.ville.currentText()
    etat = w.insc.isChecked()
    if len(id)>= 10 or not(verif(id)):
        QMessageBox.critical(w,"erreur","id doit etre une chaine alphanumerique")
    elif len(tel) != 8 or not(verif1(tel)):
        QMessageBox.critical(w,"erreur","telephone doit etre numerique")
    elif not(male or female):
        QMessageBox.critical(w,"erreur","choisir un genre")
    else : 
        f = open("clients.dat","ab")
        e = dict(client)
        e["id"] = id 
        e["tel"] = tel 
        e["ville"] = ville 
        if male : 
            e["genre"] = "Masculin"
        elif female : 
            e["genre"] =  "Feminin"
        if etat : 
            e["etat"] = "Inscrit"
        else : 
            e["etat"] = "Non Inscrit" 
        dump(e,f)
        

         
def affchance():
    f = open("chance.txt","r")
    x = f.read()
    w.chance.addItem(x)
    
def affclient():
    f = open("clients.dat","rb")
    i = 0 
    end = True
    while end :
        try: 
            x = load(f)
            w.table.insertRow(i)
            w.table.setItem(i,0, QTableWidgetItem(x["id"]))
            w.table.setItem(i,1, QTableWidgetItem(x["tel"]))
            w.table.setItem(i,2, QTableWidgetItem(x["genre"]))
            w.table.setItem(i,3, QTableWidgetItem(x["ville"]))
            w.table.setItem(i,4, QTableWidgetItem(x["etat"]))
            i =i+1
        except:
            end = False


def somme(ch):
    s = 0
    for i in range(0,len(ch)):
        s = s+int(ch[i])
    while s > 9 :
        x = str(s)
        s = 0
        for i in range(0,len(x)):
            s = s+int(x[i])
    t = open("chance.txt","r")
    p = t.readline()
    while p != "":
        if int(p) == s :
            return True
        print(int(p),s,int(p) == s, ch)
        p = t.readline()
    return False
def affgagnants():
    f = open("clients.dat","rb")
    end = True
    ch = "Les client gagnants sont :\n " 
    while end :
        try: 
            for i in range(4):
                x = load(f)
                tel = x["tel"]
                id = x["id"]
                if somme(tel) :
                    ch = ch + "Identifiant : " + id + "- N° telephone : " + tel +"\n"
        except:
            end = False
    w.gagnant.addItem(ch)


client = {
    "id" : str,
   "tel" : str,
   "ville" : str,
   "genre" : str,
   "etat" : str
}
app = QApplication([])
w = loadUi("interfaceprototype.ui")
w.pushButton_3.clicked.connect(ajouter)
w.pushButton.clicked.connect(affchance)
w.pushButton_4.clicked.connect(affclient)
w.pushButton_2.clicked.connect(affgagnants)
w.show()
app.exec_()