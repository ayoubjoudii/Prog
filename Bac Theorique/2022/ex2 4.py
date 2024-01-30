from numpy import array 
m = array([[int]*5]*5)
m = [[20,2,-5,3,2],
     [10,3,0,60,2],
     [1, 2, -3, 2, -2],
     [30, -5, 40, 50, 2],
     [-7, 4,2, 1  ,-9]]
def remplir (m, n):
    f = open("f.txt" , "w")
    f.write("Les sequence contigues des lignes"+"\n")
    for i in range(0,n):
        x = 0
        for j in range(0,n):
            x = m[i][j] 
            for g in range(j+1,n):
                x += m[i][g]
                if x == 0:  
                    f.write(str(i)+" "+str(j)+" "+str(g)+"\n")

remplir(m , 5)  
