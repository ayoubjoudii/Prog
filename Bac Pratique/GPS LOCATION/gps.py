from PyQt5.uic import * 
from PyQt5.QtWidgets import * 
from pickle import load,dump 
from math import *


def lat1(ch):
    i = 0
    k =0
    while k<2:
        if ch[i] == ',':
            k = k +1
        i = i +1
    ch1 = ch[i:]
    ch1 = ch1[:ch1.find(',')]
    print(ch1)
    dd = float(ch1[0:2])
    mm = float(ch1[2:])
    res = str(dd+mm/60)
    return res
def lat2(ch):
    p = ch.find("N")+2
    p1 = p
    while ch[p] != ",":
        p = p+1
    ch1 = ch[p1:p]
    ddd = float(ch1[:3])
    mm = float(ch1[3:])
    res = str(ddd + mm/60)
    return res
def long1(ch):
    d = float(ch)
    D = int(d)
    M = int((d-D)*60) 
    S = (d-D-M/60)*3600 
    ch1 = str(D) + "° " +str(M) + "` "+str(S)+'"'
    return ch1 
def long2(ch):
    d = float(ch)
    D= int(d)
    M= int((d-D)*60)
    S = (d-D-M/60)*3600  
    ch1 = str(D) + "° " +str(M) + "` "+str(S)+'"'
    return ch1 
def deg2rad(num):
    return num*pi/180
def calcul(lat1,long1,lat2,long2):
    sphterre=6378137 #terre=phere de 36781 km de rayon
    rlo1=deg2rad(long1)
    rla1=deg2rad(lat1)
    rlo2=deg2rad(long2)
    rla2=deg2rad(lat2)
    dlo=(rlo2-rlo1)/2
    dla=(rla2-rla1)/2
    a=sin(dla)**2+cos(rla1)*cos(rla2)*sin(dlo)**2
    d=2*atan2(sqrt(a),sqrt(1-a))
    return(sphterre*d)/1000
def trames():
    f = open("trames.txt","r")
    fb1 = open("fdd.dat","wb")
    fb2 = open("fdms.dat","wb")
    ch = f.readline()
    w.list.clear()
    i = 1
    while ch != "":
        w.list.addItem(ch)
        dd = dict(conv)
        dms = dict(conv)
        ch1 = lat1(ch)
        dd["p1"] = ch1 + "N"
        dms["p1"] = long1(ch1)
        ch2=lat2(ch)
        dd["p2"] = ch2 + "E"
        dms["p2"] = long2(ch2)
        dd["position"] = "P"+str(i)
        dms["position"] = "P"+str(i)
        dump(dd,fb1)
        dump(dms,fb2)
        ch = f.readline()
        i = i+1
    f.close()
    fb1.close()
    fb2.close()

def convertir():
    if w.dd.isChecked():
        fb1 = open("fdd.dat","rb")
    elif w.dms.isChecked():
        fb1 = open("fdms.dat","rb")
    if w.dd.isChecked() or w.dms.isChecked():
        test = True
        i = 0 
        while test :
            try :
                x = load(fb1)
                w.table.insertRow(i)
                w.table.setItem(i , 0 , QTableWidgetItem(x["position"])) 
                w.table.setItem(i , 1 , QTableWidgetItem(x["p1"])) 
                w.table.setItem(i , 2 , QTableWidgetItem(x["p2"])) 
                i = i +1
            except : 
                test = False 
        fb1.close()
    else:
        QMessageBox.critical(w,"error","3amer wahda" )
def distance():
    p1=w.p1.text()
    p2=w.p2.text()
    f=open("fdd.dat","rb")
    eof=False
    while not(eof):
        try:
            e=load(f)
            print(e["position"])
            if e["position"]==p1:
                st=e["p1"]
                sens=st[-1]
                if sens=="N":
                    lat1=float(st[:len(st)-1])
                else:
                    lat1=-float(st[:len(st)-1])
                st=e["p2"]
                if sens=="E":
                    long1=float(st[:len(st)-1])
                else:
                    long1=-float(st[:len(st)-1])
                             
            if e["position"]==p2:
                st=e["p1"]
                sens=st[-1]
                if sens=="N":
                    lat2=float(st[:len(st)-1])
                else:
                    lat2=-float(st[:len(st)-1])
                
                st=e["p2"]
                if sens=="E":
                    long2=float(st[:len(st)-1])
                else:
                    long2=-float(st[:len(st)-1])
                
                
        except:
            eof=True
    
    f.close()
    
    d=calcul(lat1,long1,lat2,long2)
    w.resultat.setText(str(d))

conv = {
    "position" : str,
    "p1" : str,
    "p2" : str
}
app = QApplication([])
w = loadUi("interface_gps.ui")
w.show()
w.trames.clicked.connect(trames)
w.conversion.clicked.connect(convertir)
w.dis.clicked.connect(distance)
app.exec_()
