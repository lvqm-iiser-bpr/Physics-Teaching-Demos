import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import TextBox
from math import pi as pi


#Define the parametrized function to be plotted.
def f(x, amplitude, wavelength, a):
    λ = wavelength
    return amplitude * np.sin(2 * np.pi * x/λ + np.pi * a)
x = np.linspace(0, 1, 1000)

#Define initial parameters
init_amplitude = 8
init_wavelength = 0.105
init_a = 0
#Creating the figure and the line that has to be manipulated.
fig, ax = plt.subplots()
line, = ax.plot( x, f(x, init_amplitude, init_wavelength, init_a), color='r')
ax.set_xlabel('x [m]', color='darkmagenta')
ax.set_ylabel('y', color='darkmagenta')
plt.style.use('fivethirtyeight')
ax.grid(True)
plt.yticks(np.arange(-15, 16, 3))
plt.title('A Wave in space, y = Ae$^{(kx+\phi)}$', fontstyle='oblique', color='navy')

#adjusting the main plot to make room for the sliders.

fig.subplots_adjust(bottom=0.40)

#Making horizontal sliders to control the wavelength, the amplitude and the phase.
axfreq =fig.add_axes([0.26, 0.07, 0.65, 0.03])
wavelength_slider = Slider(
    ax=axfreq,
    label='Wavelength (λ) [m]',
    valmin=0.015,
    valmax=0.2,
    valstep=0.01,
    valinit=init_wavelength,
)

axamp = fig.add_axes([0.26, 0.12, 0.65, 0.03])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude (A) [m]",
    valmin=1,
    valmax=15,
    valstep=1,
    valinit=init_amplitude,
)

axphi = fig.add_axes([0.26, 0.17, 0.65, 0.03])
phi_slider = Slider(
    ax=axphi,
    label='Phase Constant (Φ) [rad]',
    valmin=-2,
    valmax=2,
    valinit=init_a,
    initcolor='r',
    track_color='silver',
)
#Remove the slider text to add text box instead.

phi_slider.valtext.set_visible(False)

#ax_box = plt.axes([0.2, 0.28, 0.1, 0.07])

#Creating text box for Wavevector, Frequency and also for phase constant to show it in terms of multiples of π.

text = ax.text(-0.1,- 25, f"Wavevector (k) = {round(2*np.pi/wavelength_slider.val,2)} " "m$^{-1}$" " (where k = 2π/λ)")
text1 = ax.text(1.08, -29, f"{round(phi_slider.val, 2)} π")
text2 = ax.text(-0.1,- 22, f"Frequency (ν) = {round(1/wavelength_slider.val,2)} " "Hz" " (where ν=2π/ω=1/λ, considering wave velocity = 1m/s)")



#Defining the function to be called anytime a slider's value changes
def update(val):
    global text
    global text1
    global text2
    line.set_ydata(f(x, amp_slider.val, wavelength_slider.val, phi_slider.val))

    #Make text visible after the change in slider value to avoid overlap.
    text.set_visible(False)
    text1.set_visible(False)
    text2.set_visible(False)

    #Assuming wave velocity = 1 m/s

    #Creating text box for Wavevector, Frequency and also for phase constant.

    text = ax.text(-0.1,- 25, f"Wavevector (k) = {round(2*np.pi/wavelength_slider.val,2)} " "m$^{-1}$" " (where k = 2π/λ)")
    text1 = ax.text(1.08, -29, f"{round(phi_slider.val,2)} π")
    text2 = ax.text(-0.1, - 22, f"Frequency (ν) = {round(1 / wavelength_slider.val, 2)} " "Hz" " (where ν=2π/ω=1/λ, considering wave velocity = 1m/s)")

    fig.canvas.draw_idle()

#registering the update function with each slider

wavelength_slider.on_changed(update)
amp_slider.on_changed(update)
phi_slider.on_changed(update)

#Creating a `matplotlib.widgets.Button` to reset the sliders to initial values.

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    wavelength_slider.reset()
    amp_slider.reset()
    phi_slider.reset()
button.on_clicked(reset)

plt.show()
