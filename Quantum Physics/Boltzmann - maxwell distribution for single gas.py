import matplotlib.pyplot as plt
from scipy.constants import pi, k, R, N_A
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons

# plotting the figure
fig, ax = plt.subplots(figsize=(8,5),dpi = 100)
plt.subplots_adjust(bottom=0.25)
plt.subplots_adjust(left=0.15)

# mass used here is of Krypton
m = 1.3915 * 10 ** (-25)

# initializing the values
range_s = 2000
T_initial = 1000  # Temp in kelvin
s = np.arange(0, range_s, 1)

"defining probability distribution and plotting"

def Probability_Distribution_function(M, S, T):
    # defining constant for the boltzmann distribution formula
    c1 = 4 * pi * ((M / (2 * pi * k * T)) ** (3 / 2))  # first constant
    c2 = (M / (k * T)) / 2  # second constant
    F = c1 * (S ** 2) * np.exp(-c2 * (S ** 2))
    return F

# plotting the initial plot
f = [Probability_Distribution_function(m, S1, T_initial) for S1 in s]
ax.plot(s, f, '-', color='skyblue')

"defining the velocities and plotting them"

# most probable velocity
V_MP = ((2 * R * T_initial) / (m * N_A)) ** (0.5)

# plotting for Vmp
f_V_MP = Probability_Distribution_function(m, V_MP, T_initial)
plt.plot(V_MP, f_V_MP, 'ro', label="$V_{MP}$")

# Annotating most probable velocity
ax.annotate(f'V_MP = {V_MP:.2f} m/s', xy=(V_MP, f_V_MP),
            xytext=(-10, 30), textcoords='offset points',fontsize= 8,bbox = dict(facecolor='red', alpha=0.5))

# average velocity
V_AVG = ((8 * R * T_initial)/(pi * m * N_A))**(0.5)

#plotting for Vavg
f_V_AVG = Probability_Distribution_function(m, V_AVG, T_initial)
plt.plot(V_AVG, f_V_AVG, 'yo', label="$V_{AVG}$")

# Annotating most probable velocity
ax.annotate(f'V_AVG = {V_AVG:.2f} m/s', xy=(V_AVG, f_V_AVG),
            xytext=(0, 20), textcoords='offset points',fontsize= 8,bbox = dict(facecolor='yellow', alpha=0.5))

# RMS velocity
V_RMS = ((3 * R * T_initial) / (m * N_A)) ** (0.5)

# plotting for Vrms
f_V_RMS = Probability_Distribution_function(m, V_RMS, T_initial)
plt.plot(V_RMS, f_V_RMS, 'go', label="$V_{RMS}$")

# Annotating RMS velocity
ax.annotate(f'V_RMS = {V_RMS:.2f} m/s', xy=(V_RMS, f_V_RMS),
            xytext=(10, 10), textcoords='offset points',fontsize= 8,bbox = dict(facecolor='green', alpha=0.5))


# temp slider
slider_ax_temp = plt.axes([0.2, 0.05, 0.63, 0.06])
slider_temp = Slider(slider_ax_temp, "Temperature (K)", 1, 10000, valinit=1000, valstep=100)

# Labels, Title, Grid, and Limit
ax.legend()
ax.grid(True)
ax.set_xlabel('Speed (m/s)')
ax.set_ylabel('Probability Density (s/m)')
plt.suptitle('Maxwell–Boltzmann Distribution', bbox=dict(facecolor='black', alpha=0.5))
ax.set_ylim(0.000, 0.005)


# filling the area under the curve
ax.fill_between(s, f, alpha=0.25)

def update(val):
    # slider value uptake
    T = slider_temp.val

    global range_s,s            # global variable

    "updtaing the velocities"
    V_RMS = ((3 * R * T) / (m * N_A)) ** (0.5)
    V_MP = ((2 * R * T) / (m * N_A)) ** (0.5)
    V_AVG = ((8 * R * T) / (pi * m * N_A)) ** (0.5)

    # calling Probability Distribution/Density Function
    f = [Probability_Distribution_function(m, S, T) for S in s]

    ax.cla()                             # clearing the axis

    # plotting the axis
    ax.plot(s, f, '-', color='skyblue')

    "Vmp"
    # plotting for Vmp
    ax.plot(V_MP, Probability_Distribution_function(m, V_MP, T), 'ro', label="$V_{MP}$")

    # Annotating most probable velocity
    ax.annotate(f'V_MP = {V_MP:.2f} m/s', xy=(V_MP, Probability_Distribution_function(m, V_MP, T)),
                xytext=(-10, 30), textcoords='offset points',fontsize= 8,bbox = dict(facecolor='red', alpha=0.5))

    "Vavg"
    # plotting for Vavg
    ax.plot(V_AVG, Probability_Distribution_function(m, V_AVG, T), 'yo', label="$V_{AVG}$")

    # Annotating most probable velocity
    ax.annotate(f'V_AVG = {V_AVG:.2f} m/s', xy=(V_AVG, Probability_Distribution_function(m, V_AVG, T)),
                xytext=(0, 20), textcoords='offset points',fontsize= 8,bbox = dict(facecolor='yellow', alpha=0.5))

    "Vrms"
    # plottitng Vrms velocity
    ax.plot(V_RMS, Probability_Distribution_function(m, V_RMS, T), 'go', label="$V_{RMS}$")

    # Annotating RMS velocity
    ax.annotate(f'V_RMS = {V_RMS:.2f} m/s', xy=(V_RMS, Probability_Distribution_function(m, V_RMS, T)),
                xytext=(10, 10), textcoords='offset points',fontsize= 8,bbox = dict(facecolor='green', alpha=0.5))


    # filling the area under the curve
    ax.fill_between(s, f, alpha=0.25)

    # Labels, Title, Grid, and Limit
    ax.legend()
    ax.grid(True)
    ax.set_xlabel('Speed (m/s)')
    ax.set_ylabel('Probability Density (s/m)')
    plt.suptitle('Maxwell–Boltzmann Distribution', bbox=dict(facecolor='black', alpha=0.5))
    ax.set_ylim(0.000, 0.005)

# updating value from the slider
slider_temp.on_changed(update)

# Adding the reset button
reset = plt.axes([0.8, 0.13, 0.1, 0.04])
button = Button(reset, 'Reset', color='gold', hovercolor='red')

# function to reset
def resetslider(event):
    slider_temp.reset()

# calling reset slider
button.on_clicked(resetslider)


plt.show()
