import matplotlib.pyplot as plt
from scipy.constants import pi, k
import numpy as np
from matplotlib.widgets import Slider,Button,RadioButtons

"plotting the figure"
fig,ax = plt.subplots(figsize=(12,5),dpi=100)
plt.subplots_adjust(bottom=0.30)
plt.subplots_adjust(left=0.15)

"initializing the mass of different gases"
MASS_OF_GAS=[6.646 * 10 ** (-27), 3.3509 * 10 **(-26), 6.6335 * 10 ** (-26), 1.3915 * 10 ** (-25), 2.1801 * 10 ** (-25)]                # mass in gram
mass_He = MASS_OF_GAS[0]
mass_Ne = MASS_OF_GAS[1]
mass_Ar = MASS_OF_GAS[2]
mass_Kr = MASS_OF_GAS[3]
mass_Xe = MASS_OF_GAS[4]

"initializing the values"
range_s = 4500
T_initial = 300         # Temp in kelvin
s = np.arange(0,range_s,1)


def Probability_Distribution_function(M,S,T):
    'defining constant for the boltzman distribution formula'
    c1 = 4 * pi * ((M / (2 * pi * k * T)) ** (3 / 2))  # first constant
    c2 = (M /(k*T)) / 2                               # second constant
    F = c1 * (S**2) * np.exp(-c2 * (S**2))
    return F

"adding axis for slider and adding the slider"

# temp slider
slider_ax_temp = plt.axes([0.2,0.07,0.55,0.05])
slider_temp = Slider(slider_ax_temp,"Temprature(K)",1,4000,valinit=300,valstep=50)

"plotting the initial plot and filling the area under the curve with tranparency"

# for helium
f_He = [Probability_Distribution_function(mass_He,S1,T_initial) for S1 in s]
ax.plot(s, f_He, '-',color = 'red',label="Helium")
ax.fill_between(s,f_He,color = 'red',alpha = 0.20)

# for Neon
f_Ne = [Probability_Distribution_function(mass_Ne,S1,T_initial) for S1 in s]
ax.plot(s, f_Ne, '-', color = 'orange',label="Neon")
ax.fill_between(s,f_Ne,color = 'orange',alpha = 0.20)

# for Argon
f_Ar = [Probability_Distribution_function(mass_Ar,S1,T_initial) for S1 in s]
ax.plot(s, f_Ar, '-', color = 'violet',label="Argon")
ax.fill_between(s,f_Ar,color = 'violet',alpha = 0.20)

# for krypton
f_Kr = [Probability_Distribution_function(mass_Kr,S1,T_initial) for S1 in s]
ax.plot(s, f_Kr, '-', color = 'green',label="Krypton")
ax.fill_between(s,f_Kr,color = 'green',alpha = 0.20)

# for Xenon
f_Xe = [Probability_Distribution_function(mass_Xe,S1,T_initial) for S1 in s]
ax.plot(s, f_Xe, '-', color = 'blue',label="Xenon")
ax.fill_between(s,f_Xe,color = 'blue',alpha = 0.20)


"Labels , Title , Grid and limit"
ax.legend()
ax.grid(True)
ax.set_xlabel('speed(m/s)')
ax.set_ylabel('Probabiility Density (s/m)')
plt.suptitle('Maxwell–Boltzmann distribution for Noble gases',bbox=dict(facecolor='black', alpha=0.5))
ax.set_ylim(0.000,0.005)


def update(val):
    "slider value uptake"
    T = slider_temp.val

    global range_s,s


    "calling Probablity Distribution/Density Function"
    f_He = [Probability_Distribution_function(mass_He, S, T) for S in s]
    f_Ne = [Probability_Distribution_function(mass_Ne, S, T) for S in s]
    f_Ar = [Probability_Distribution_function(mass_Ar, S, T) for S in s]
    f_Kr = [Probability_Distribution_function(mass_Kr, S, T) for S in s]
    f_Xe = [Probability_Distribution_function(mass_Xe, S, T) for S in s]


    "redrawing the updated plot"
    ax.cla()
    ax.plot(s, f_He, '-', color = 'red', label="Helium")
    ax.plot(s, f_Ne, '-', color = 'orange', label="Neon")
    ax.plot(s, f_Ar, '-', color= 'violet', label="Argon")
    ax.plot(s, f_Kr, '-', color='green', label="Krypton")
    ax.plot(s, f_Xe, '-', color='blue', label="Xenon")

    "filling area under the curve"
    ax.fill_between(s, f_He, color='red', alpha=0.20)
    ax.fill_between(s, f_Ne, color='orange', alpha=0.20)
    ax.fill_between(s, f_Ar, color='violet', alpha=0.20)
    ax.fill_between(s, f_Kr, color='green', alpha=0.20)
    ax.fill_between(s, f_Xe, color='blue', alpha=0.20)


    "Labels , Title , Grid and limit"
    ax.legend()
    ax.grid(True)
    ax.set_xlabel('speed(m/s)')
    ax.set_ylabel('Probabiility Density (s/m)')
    plt.suptitle('Maxwell–Boltzmann distribution for Noble gases', bbox=dict(facecolor='black', alpha=0.5))
    ax.set_ylim(0.000, 0.005)
    #ax.set_xlim(0,5000)

"updating value from the slider"
slider_temp.on_changed(update)

"Adding the reset button"
reset = plt.axes([0.8, 0.16, 0.1, 0.04])
button = Button(reset, 'Reset', color='gold',
                hovercolor='red')

"function to reset"
def resetslider(event):
    slider_temp.reset()

'''calling reset slider'''
button.on_clicked(resetslider)


plt.show()
