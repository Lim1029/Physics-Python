#Using template provided by Dr, thank you Dr
#LIM MING KANG
#U2004991

import numpy as np

import matplotlib.pyplot as mpl

def f(x):
    return np.sin(x)

def fp(x):
    return np.cos(x)

def fpp(x):
    return -np.sin(x)

x = 0.5


for i in range (0,10):
    xi = x - f(x)/fp(x) 
    delx = abs(xi-x)  
    if delx < 10**(-5):
       print ('stop calculation')
       break
    else:
       print(i,xi,f(x),delx)
       mpl.plot(x,f(x),'bx--') 
    x = xi 

x = np.arange(-10,10,0.0001)

mpl.title ('Newton Method for Optimisation')
mpl.xlabel('x-axis')
mpl.ylabel ('y-axis')
mpl.plot(x,f(x),'g-')
mpl.show()
