import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.widgets import Slider,Button
from mpmath import *

#Saimurali

"""
equation demonstrated in this code

tan(z) = SQRT((Z_0/Z)^2 - 1)
-cot(z) = SQRT((Z_0/Z)^2 - 1)
"""



fig = figure(figsize=(8,10))
plt.subplots_adjust(bottom=0.25)

#Arbitary Values
a = 1   #length of well

v = 1  #potential

m = 1

z_0 = (a) * np.sqrt(2 * m * v)




def eq(x,n):
    """

    :param x: Z_0
    :param n: Z
    :return: SQRT{(z_0/z)^2 - 1}
    """
    return np.sqrt((((n/x)**2) - 1))



n = 1001

z = np.linspace(0* np.pi, 5 * np.pi,n)

x_0_tan = np.linspace(0,0.5,n) * np.pi
x_1_tan = np.linspace(1,1.5,n) * np.pi
x_2_tan = np.linspace(2,2+0.5,n) * np.pi


x_0_cot = np.linspace(0.5,1,n) * np.pi
x_1_cot = np.linspace(1.5,2,n) * np.pi
x_2_cot = np.linspace(2.5,3,n) * np.pi


cot_check =[]
for i in range(len(x_0_cot)):
    cot_check.append(cot(x_0_cot[i]))

cot_graph = np.asarray(cot_check)






plt.plot(x_0_tan,np.tan(x_0_tan), color='blue',label=r"$tan(z)$")
plt.plot(x_1_tan,np.tan(x_0_tan), color='blue')
plt.plot(x_2_tan,np.tan(x_0_tan), color='blue')


plt.plot(x_0_cot,-cot_graph, color='red',label=r'$-cot(z)$')
plt.plot(x_1_cot,-cot_graph, color='red')
plt.plot(x_2_cot,-cot_graph, color='red')

plt.title("Finite Square Well Solutions (Bound States)")

#Changing X-axis ticks
plt.xticks([0,0.5*np.pi,1*np.pi,1.5*np.pi,2*np.pi,2.5*np.pi,3*np.pi,3.5*np.pi,4*np.pi,4.5*np.pi,5*np.pi],
           ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$",r"$\frac{5\pi}{2}$",r"$3\pi$",r"$\frac{7\pi}{2}$",
            r"$4\pi$",r"$\frac{9\pi}{2}$",r"$5\pi$"])

#Removing Y-axis ticks
ax = plt.gca()
ax.yaxis.set_tick_params(labelleft=False)


#Plotting curve SQRT{(z_0/z)^2 - 1}
p1,=plt.plot(z,eq(z,1*np.pi),label=r'$\sqrt{(z_0/z)^2 - 1}$')
plt.xlabel("Z")

#Use full screen for proper orientation
plt.text(0.8,-6,f"Shallow/ \nNarrow Well")
plt.text(9.2,-6,f"Wide/ \nDeep Well")
plt.legend(loc=1)


plt.ylim(0,20) #Do not remove, else you will get delta functions
plt.xlim(0,10)

#Creating Slider
axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])
sp_slider = Slider(
                ax=axSlider_1,
                label=r"$Z_0$",
                valmin=1,
                valmax=30,
                valinit=1*np.pi,
                valstep=0.5,
                closedmin=True,
                closedmax=True

)

#Updating Slider
def update(value):
    z_0_change = sp_slider.val

    p1.set_ydata(eq(z,z_0_change))

    fig.canvas.draw_idle()


sp_slider.on_changed(update)


plt.show()
