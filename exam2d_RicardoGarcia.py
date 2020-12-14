"""
Examen 2D graficacion
Ricardo Gabriel Garcia Gomez
Num control:18390026
"""

import numpy as np
import matplotlib.pyplot as plt 
import math as mt

plt.axis([0,150,0,150])
plt.axis('on')
plt.grid(True)
plt.title('Examen 2D')
plt.axes().set_aspect('equal')

#punto 8, colores basado del numero de control
clr = (0/10,2/10,6/10)
#circulo

#ultimo digito del numero de control
ultdig=6
#punto 5 calculo del radio
r=ultdig*5
#centro del circulo
xc=100
yc=100

p1=0*np.pi/180
p2=360*np.pi/180
dp = (p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
#plotea el circulo
for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=clr)
    xlast=xp
    ylast=yp

#primer rectangulo
#punto 3, se hace el calculo de los puntos segun el centro y el radio del circulo
x=np.array([xc,xc,xc-2*r,xc-2*r,xc])
y=np.array([yc,yc-2*r,yc-2*r,yc,yc])
plt.plot(x,y, color=clr)
#se cambian los valores del centro para trasladar el segundo rectangulo
xc=xc*1.3
yc=yc*1.3
#segundo rectangulo
x=np.array([xc,xc,xc-2*r,xc-2*r,xc])
y=np.array([yc,yc-2*r,yc-2*r,yc,yc])
plt.plot(x,y, color=clr)

plt.show()