from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
def puis(x,y):
    if y == 0:
        return 1
    else : 
        return puis(x,y-1)*x

def transformer(x):
    n = 1 
    if len(str(x))%2 == 1:
        ch = str(x) + "1"
        for i in range(0,len(ch)-1,2):
            if ch[i]+ch[i+1] != "00":
                n = n * puis(int(ch[i]) , int(ch[i+1]))
    else: 
        ch = str(x)
        for i in range(0,len(ch)-1,2):
            if ch[i]+ch[i+1] != "00":
                n = n * puis(int(ch[i]) , int(ch[i+1]))
    return str(n)
def chercher(n,m):
    ch = transformer(int(n))
    for i in range(int(m)):
        ch = ch+"-"+transformer(int(n)+i+1)
    return ch

def play():
    n = w.ntext.text()
    m = w.mtext.text()
    if not(n.isnumeric() and 200<=int(n)<=999999) or not (m.isnumeric() and 3<=int(m)<=10):
        w.res.setText("n un entier entre 200 et 999999 et m un entier entre 3 et 10")
    else: 
        w.res.setText(chercher(n,m))

        
        

app = QApplication([])
w = loadUi("interfacepowertrain.ui")
w.show()
w.trans.clicked.connect(play)
app.exec_()