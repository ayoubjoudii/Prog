from PyQt5.uic import * 
from PyQt5.QtWidgets import * 

def etape1(x):
    ch = ""
    for i in range(len(x)):
        ch = ch + str(int(x[i])%7)
    return ch 
def etape2(y):
    z = ""
    if len(y) % 2 != 0:
        y = y[1:]
        for i in range(len(y)-1,-1,-2):
            z = str(int(y[i-1]+y[i])%7) +z
        return (y[0]+z)
    else:
        for i in range(len(y)-1,-1,-2):
            z = str(int(y[i-1]+y[i])%7) +z
        return (z)
def horner(z):
    m = 0
    while z != "":
        ch = z[0]
        m = (m*2 + int(ch)) % 7
        z = z[1:len(z)]
    return m 
def play():
    x = w.textx.text()
    if x == "" or x.isnumeric()==False or len(x)<5 or len(x)>20:
        w.res.setText('vuiller sais entre 5 a 20')
    else : 
        w.res.setText(str(horner(etape2(etape1(x)))))

app = QApplication([])
w = loadUi("interfacehorner.ui")
w.show()
w.verif.clicked.connect(play)
app.exec_()