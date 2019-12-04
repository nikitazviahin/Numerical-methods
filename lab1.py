import math
import pylab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
x = -1.0
i = 0
arrx = []
arry = []
while i < 21:
    y =(5*(x**3)-4*x+2)**(0.5)
    print(y)
    arrx.append(x)
    arry.append(y)
    x = x + 0.1
    i = i + 1

def lagranz(arrx,arry,t): 
         z=0
         for j in range(len(arry)):
             p1=1; p2=1
             for i in range(len(arrx)):
                 if i==j:
                     p1=p1*1; p2=p2*1   
                 else: 
                     p1=p1*(t-arrx[i])
                     p2=p2*(arrx[j]-arrx[i])
             z = z+arry[j]*p1/p2
         return z
t = -1.0
i = 0
newarrx = []
newarry = []
while i < 101:
    newarrx.append(t)
    newarry.append(lagranz(arrx,arry,t))
    t = t + 0.02
    i += 1






