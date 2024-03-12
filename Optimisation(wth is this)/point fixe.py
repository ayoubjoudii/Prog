# point fixe : f(x)=x , y = x
import math
ep = 0.00001
def f(x) : 
    return x*x - 2
def fixe(ep):#positive
    x = 0
    while abs(f(x)-x) > ep:
        x = f(x)
    return x 
def zero(a,b,ep):
    m = (b-a)/2 #milieu intervalle
    while abs(b-a) > ep and f(m) != 0:
        if f(a)*f(m) > 0 : # f(x) ya < 0 wala > 0
            a = m #a       m       b --> (old)a    a=m     b 
        else : 
            b = m #a      m      b --> a    b=m   (old)b 
        m = (b-a)/2 
    return m     
             

