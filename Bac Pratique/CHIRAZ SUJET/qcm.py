from pickle import dump,load
from numpy import array 

n = int(input("saisir n : "))
while not(2<= n <= 10):
    n = int(input("saisir n : "))
f = open("resultat.dat" , "wb")
fb = open("test.dat" , "rb")
test = True
while test : 
    try : 
        x = load(fb)
        print(x)
    except:
        test = False

t = array([bool]*10)

print(type(x["rep"]))