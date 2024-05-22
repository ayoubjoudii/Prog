from PyQt5.uic import * 
from PyQt5.QtWidgets import * 

def sommechiffres(x):
    s = 0
    while x!= 0 :
        s = s+x%10
        x = x//10
    return s
    
def verifier(n):
    test  = False
    for i in range(1,n+1):
        if sommechiffres(i)+i == n:
            test = True
    return test
def chercher(n,m):
    ch = ""
    for i in range(n,m+1):
        if verifier(i) == False:
            ch = ch + str(i) + "-"
    return ch  
def play():
    n = w.textn.text()
    m = w.textm.text()
    if n == "" or n.isdecimal() == False or int(n) < 20 or int(n) >50:
        w.res.setText("tfaked l n")
    elif m == "" or m.isdecimal() == False or int(m) < int(n) or int(m) >100:
        w.res.setText("tfaked l M")
    else : 
        if chercher(int(n),int(m)) == "":
            w.res.setText("aucun nombre entre " + n + " et " + m)
        else: 
            w.res.setText("Les nombres autonombres: "+chercher(int(n),int(m))[:-1])

            

app = QApplication([])
w = loadUi("interfacenombre.ui")
w.show()
w.afficher.clicked.connect(play)
app.exec_()