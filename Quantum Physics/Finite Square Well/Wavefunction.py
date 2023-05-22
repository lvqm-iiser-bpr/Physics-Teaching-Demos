import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.widgets import Slider,Button
from mpmath import *

#Saimurali

L = 20
n = 1001
a = L/2



x = np.linspace(0,L,n)

x_left = np.linspace(-1.5*L,-L/2,n)
x_mid = np.linspace(-a,a,n)
x_right = np.linspace(L/2,1.5*L,n)


def eq(x,n):
    """

    :param x: Z_0
    :param n: Z
    :return: SQRT{(z_0/z)^2 - 1}
    """
    return np.sqrt((((n/x)**2) - 1))

m = 1
h_bar = 1



"""Initializing intersection points and required constants"""
inter_cos=np.asarray([2.3,1.126,0.815])
z_0_cos = np.asarray([3,6,9])

inter_sin=np.asarray([1.274,1.047,0.967])
z_0_sin = np.asarray([4,8,12])

z_0_cos_boundary=np.asarray([1,3.3,6.4])
z_0_sin_boundary=np.asarray([1.7,4.8,8])

z_cos = z_0_cos/(np.sqrt((inter_cos**2) + 1))
l_cos =z_cos/a
k_cos = l_cos*np.tan(l_cos*a)
c_cos = 0.5*np.cos(l_cos*a)

z_sin = z_0_sin/(np.sqrt((inter_sin**2) + 1))
l_sin =z_sin/a
k_sin=[]
for i in range(len(l_sin)):
    k_sin.append(-l_sin[i] * cot(l_sin[i] * a))

k_sin_2= np.asarray(k_sin)

k_sin = np.asarray([0.310566446822029,0.58407474923357883,0.8405736931220763])
c_sin = 0.5*np.sin(l_sin*a)








def solution_cos(n,depth):
    """

    :param n: Variable to access array(s)
    :param depth: increases the depth of the well
    :return: depth
    """
    n=n-1
    ax2.plot(x_mid, 0.5 * np.cos(l_cos[n] * x_mid) - depth, color="blue")
    ax2.plot(x_left, expo(x_left + a, c_cos[n], k_cos[n]) - depth, color='blue')
    ax2.plot(x_right, expo(x_right - a, c_cos[n], -k_cos[n]) - depth, color='blue')

    depth = depth + 1.5

    return depth

def solution_sin(n,depth):
    """

    :param n: Variable to access array(s)
    :param depth: increases the depth of the well
    :return: depth
    """
    n = n - 1
    ax2.plot(x_mid, 0.5 * np.sin(l_sin[n] * x_mid) - depth, color="red")
    ax2.plot(x_left, expo(x_left + a, -c_sin[n], k_sin[n]) - depth, color='red')
    ax2.plot(x_right, expo(x_right - a, c_sin[n], -k_sin[n]) - depth, color='red')

    depth = depth + 1.5

    return depth



def expo(x,const,power):
    return const * np.exp(power*x)


"""Plotting tan(z) and -cot(z)"""
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

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(6,6))
plt.subplots_adjust(bottom=0.25)

ax1.plot(x_0_tan,np.tan(x_0_tan), color='blue',label=r"$tan(z)$")
ax1.plot(x_1_tan,np.tan(x_0_tan), color='blue')
ax1.plot(x_2_tan,np.tan(x_0_tan), color='blue')
ax1.plot(x_0_cot,-cot_graph, color='red',label=r'$-cot(z)$')
ax1.plot(x_1_cot,-cot_graph, color='red')
ax1.plot(x_2_cot,-cot_graph, color='red')
p1,=ax1.plot(z,eq(z,1.5),color="black",label=r'$\sqrt{(z_0/z)^2 - 1}$') #
ax1.set_title("Finite Square Well Solutions (Bound States)")
ax1.set_ylim(0,20)
ax1.legend(loc='upper right')
ax1.set_xticks([0,0.5*np.pi,1*np.pi,1.5*np.pi,2*np.pi,2.5*np.pi],
           ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$",r"$\frac{5\pi}{2}$"])




"""PLotting finite well with wavefunction(s)"""
depth = 1

ax2.plot(x_mid, 0.5 * np.cos(l_cos[0] * x_mid) - depth, color="blue")
ax2.plot(x_left, expo(x_left + a, c_cos[0], k_cos[0]) - depth, color='blue')
ax2.plot(x_right, expo(x_right - a, c_cos[0], -k_cos[0]) - depth, color='blue')

ax2.axvline(-L / 2, ymax=0.956)
ax2.axvline((L / 2), ymax=0.956)
ax2.axhline(0, xmin=0.65)
ax2.axhline(0, xmax=0.35)
ax2.set_title("Bound States Wavefunction(s)")
ax2.text(-8,-0.08,f"V(x)")
ax2.set_xticks([-L/2,L/2],[r'$-\frac{L}{2}$',r'$\frac{L}{2}$'])


ax1.yaxis.set_tick_params(labelleft=False)
ax2.yaxis.set_tick_params(labelleft=False)

"""Constructing Slider"""
axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])
sp_slider = Slider(
                ax=axSlider_1,
                label=r"$Z_0$",
                valmin=1,
                valmax=8.5,
                valinit=1.5,
                valstep=0.1,
                closedmin=True,
                closedmax=True

)

def update(value):
    z_0_change = sp_slider.val


    ax2.clear()


    p1.set_ydata(eq(z,z_0_change))

    """Clearing and re-plotting wavefunction(s) plots"""

    if z_0_cos_boundary[0]<=z_0_change<z_0_sin_boundary[0]:
        a=solution_cos(1, 1)

    if z_0_sin_boundary[0]<=z_0_change<z_0_cos_boundary[1]:
        a=solution_sin(1, 1)
        b=solution_cos(1,a)


    if z_0_cos_boundary[1]<= z_0_change < z_0_sin_boundary[1]:
        a= solution_cos(2,1)
        b = solution_sin(1, a)
        c = solution_cos(1, b)

    if z_0_sin_boundary[1]<=z_0_change<z_0_cos_boundary[2]:
        a = solution_sin(2,1)
        b = solution_cos(2,a)
        c = solution_sin(1,b)
        d = solution_cos(1,c)

    if z_0_cos_boundary[2]<=z_0_change<z_0_sin_boundary[2]:
        a = solution_cos(3,1)
        b = solution_sin(2,a)
        c = solution_cos(2,b)
        d = solution_sin(1,c)
        e = solution_cos(1,d)

    if z_0_change>=z_0_sin_boundary[2]:
        a = solution_sin(3,1)
        b = solution_cos(3,a)
        c = solution_sin(2,b)
        d = solution_cos(2,c)
        e = solution_sin(1,d)
        f = solution_cos(1,e)



    ax2.axvline(-L / 2,ymax=0.956)
    ax2.axvline((L / 2),ymax=0.956)
    ax2.axhline(0,xmin=0.65)
    ax2.axhline(0, xmax=0.35)
    ax2.text(-8,-0.08,f"V(x)")
    ax2.set_title("Bound States Wavefunction(s)")
    ax2.set_xticks([-L / 2, L / 2], [r'$-\frac{L}{2}$', r'$\frac{L}{2}$'])
    ax2.yaxis.set_tick_params(labelleft=False)


    fig.canvas.draw_idle()


sp_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    sp_slider.reset()
button.on_clicked(reset)

plt.show()
