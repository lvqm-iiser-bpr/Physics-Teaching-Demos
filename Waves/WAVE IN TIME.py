import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import TextBox
from math import pi as pi


# Define the parametrized function to be plotted.
def f(t, amplitude, frequency, x):
    ν = frequency
    return amplitude * np.sin( 2 * np.pi * ν * t + x * np.pi)
t = np.linspace(0, 1, 1000)


# Define initial parameters
init_amplitude = 8
init_frequency = 8
init_x = 0
# Creating the figure and the line that has to be manipulated.
fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency, init_x), color='r')
ax.set_xlabel('Time [s]', color='darkmagenta')
ax.set_ylabel('y', color='darkmagenta')
plt.style.use('fivethirtyeight')
ax.grid(True)

plt.yticks(np.arange(-15, 16, 3))
plt.title('A Wave in time, y = Ae$^{(iωt+Φ)}$', fontstyle='oblique', color='navy')


# adjusting the main plot to make room for the sliders.

fig.subplots_adjust(bottom=0.40)

# Making horizontal sliders to control the frequency, the amplitude and the phase.

axfreq =fig.add_axes([0.28, 0.08, 0.62, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency (ν) [Hz]\n (where ν=ω/2π)',
    valmin=0.0,
    valmax=50,
    valstep=0.5,
    valinit=init_frequency,
)

axamp = fig.add_axes([0.28, 0.15, 0.62, 0.03])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude (A) [m]",
    valmin=1,
    valmax=15,
    valstep=1,
    valinit=init_amplitude,
)

axphi = fig.add_axes([0.28, 0.20, 0.62, 0.03])
phi_slider = Slider(
    ax=axphi,
    label='Phase Constant (Φ) [rad]',
    valmin=-2,
    valmax= 2,
    valinit=init_x,
)

# Remove the slider text to add text box instead.

phi_slider.valtext.set_visible(False)

#Creating text box for phase constant to show it in terms of multiples of π

text1 = ax.text(1.06,-27.5,f"{phi_slider.val} π")

#ax_box = plt.axes([0.2, 0.28, 0.1, 0.07])
#textbox = TextBox(ax_box, f'Wavelength (in m) = {freq_slider.val}')

# Creating text box for time period
text = ax.text(-0.1,-23,f"Time Period (T) = {round(1/freq_slider.val,2)} s" " ( where T = 1/ν = λ, considering wave velocity = 1 m/s)")

# Defining the function to be called anytime a slider's value changes.

def update(val):
    global text1
    global text
    line.set_ydata(f(t, amp_slider.val, freq_slider.val, phi_slider.val))
    text.set_visible(False)

    #Updating text box for time period
    text = ax.text(-0.1,-23, f"Time Period (T) = {round(1 / freq_slider.val, 2)} s" " ( where T = 1/ν = λ, considering wave velocity = 1 m/s)")
    text1.set_visible(False)

    #Updatting text box for phase constant
    text1 = ax.text(1.06, -27.5, f"{round(phi_slider.val,2)} π")

    fig.canvas.draw_idle()


# registering the update function with each slider.

freq_slider.on_changed(update)
amp_slider.on_changed(update)
phi_slider.on_changed(update)

# Creating a `matplotlib.widgets.Button` to reset the sliders to initial values.

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    freq_slider.reset()
    amp_slider.reset()
    phi_slider.reset()
button.on_clicked(reset)

plt.show()
