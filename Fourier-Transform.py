import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import TextBox
import scipy.fftpack

# Number of samplepoints
N = 1000
# sample spacing
T = 1 / 125
x = np.linspace(0.0,N*T,N)  #0.0,10,1000 values distribute

#x = np.arange(0,3,0.1) #value of x axis
def f(x, a1, a2, a3, a4, f1, f2, f3, f4):
    return a1*np.sin(2*np.pi*f1*x) + a2*np.sin(2*np.pi*f2*x) + a3*np.cos(2*np.pi*f3*x) + a4*np.cos(2*np.pi*f4*x)

init_a1=10
init_a2=20
init_a3=30
init_a4=40
init_f1= 1
init_f2= 3
init_f3= 5
init_f4= 7

#Plot the original signal
fig=plt.figure()
u = fig.add_axes([0.130, 0.26, 0.340, 0.65])
uu,=u.plot(x,f(x,init_a1,init_a2,init_a3,init_a4,init_f1,init_f2,init_f3,init_f4),color='crimson')
u.set_xlim(0,4)


u.set_xlabel('x [m]', color='darkmagenta',fontsize= '12')
u.text(-0.375,12.5, 'y[m]', color='darkmagenta',fontsize= '12')
u.set_title('ORIGINAL SIGNAL\ny=A$_1$sin(2πv$_1$x)+Α$_2$sin(2πν$_2$x)+Α$_3$cos(2πν$_3$x)+Α$_4$cos(2πν$_4$x)', color="b")

# Making horizontal sliders to control the amplitudes and vertical ones to control the frequencies.
ua1 =fig.add_axes([0.115, 0.16, 0.35, 0.03])
a1_slider = Slider(
    ax=ua1,
    label='A$_1$ [m]',
    valmin=0,
    valmax=50,
    valstep=0.1,
    valinit=init_a1,
    facecolor='purple',
    edgecolor='black'
)

ua2 =fig.add_axes([0.115, 0.13, 0.35, 0.03])
a2_slider = Slider(
    ax=ua2,
    label='A$_2$ [m]',
    valmin=0,
    valmax=50,
    valstep=0.1,
    valinit=init_a2,
    facecolor='purple',
    edgecolor='black'
)

ua1 =fig.add_axes([0.115, 0.10, 0.35, 0.03])
a3_slider = Slider(
    ax=ua1,
    label='A$_3$ [m]',
    valmin=0,
    valmax=50,
    valstep=0.1,
    valinit=init_a3,
    facecolor='purple',
    edgecolor='black'
)

ua4 =fig.add_axes([0.115, 0.07, 0.35, 0.03])
a4_slider = Slider(
    ax=ua4,
    label='A$_4$ [m]',
    valmin=0,
    valmax=50,
    valstep=0.1,
    valinit=init_a4,
    facecolor='purple',
    edgecolor='black'
)

uf4 =fig.add_axes([0.085, 0.26, 0.015, 0.60])
f4_slider = Slider(
    ax=uf4,
    label='ν$_4$\n[Hz]',
    valmin=0,
    valmax=10,
    valstep=0.1,
    valinit=init_f4,
    orientation='vertical',
    facecolor='gold',
    edgecolor='black'
)
uf3=fig.add_axes([0.060, 0.26, 0.015, 0.60])
f3_slider = Slider(
    ax=uf3,
    label='ν$_3$\n[Hz]',
    valmin=0,
    valmax=10,
    valstep=0.1,
    valinit=init_f3,
    orientation='vertical',
    facecolor='gold',
    edgecolor='black'
)
uf2 =fig.add_axes([0.035, 0.26, 0.015, 0.60])
f2_slider = Slider(
    ax=uf2,
    label='ν$_2$\n[Hz]',
    valmin=0,
    valmax=10,
    valstep=0.1,
    valinit=init_f2,
    orientation='vertical',
    facecolor='gold',
    edgecolor='black'
)
uf1 =fig.add_axes([0.01, 0.26, 0.015, 0.60])
f1_slider = Slider(
    ax=uf1,
    label='ν$_1$\n[Hz]',
    valmin=0,
    valmax=10,
    valstep=0.1,
    valinit=init_f1,
    orientation='vertical',
    facecolor='gold',
    edgecolor='black'
)
u1 = fig.add_axes([0.535, 0.1, 0.425, 0.85])
fig.subplots_adjust(bottom=0.26)
wave_sum = f(x, a1_slider.val, a2_slider.val, a3_slider.val, a4_slider.val, f1_slider.val, f2_slider.val, f3_slider.val, f4_slider.val)
yf = scipy.fftpack.fft(wave_sum)
xf = np.linspace(0.0, 1.0/T, N//2)

def g(wave_sum,N):
    wave_sum = f(x, a1_slider.val, a2_slider.val, a3_slider.val, a4_slider.val, f1_slider.val, f2_slider.val,
                 f3_slider.val, f4_slider.val)
    N = 1000
    return 4.0/N * np.abs(scipy.fftpack.fft(wave_sum[:N//2]))

#Plot the Fourier Transform of the Original Signal
aa,=u1.plot(xf, g(wave_sum,N),color='darkblue')
u1.set_xlabel("Frequency(ν)", color='darkred', fontsize='20'),
u1.set_ylabel("Amplitude(A)", color='darkred', fontsize='20'),
u1.set_xlim(-0.001,8),
u1.set_ylim(-0.1,155),
u1.set_title('FOURIER TRANSFORM', color='darkgreen')

def update(val):
    uu.set_ydata(f(x, a1_slider.val, a2_slider.val, a3_slider.val, a4_slider.val, f1_slider.val, f2_slider.val,
                 f3_slider.val, f4_slider.val))
    aa.set_ydata(g(wave_sum=f(x, a1_slider.val, a2_slider.val, a3_slider.val, a4_slider.val, f1_slider.val, f2_slider.val,
                 f3_slider.val, f4_slider.val),N=N))

#Registering the update function with each slider

a1_slider.on_changed(update)
a2_slider.on_changed(update)
a3_slider.on_changed(update)
a4_slider.on_changed(update)
f1_slider.on_changed(update)
f2_slider.on_changed(update)
f3_slider.on_changed(update)
f4_slider.on_changed(update)

resetax1 = fig.add_axes([0.0125, 0.170, 0.058, 0.04])
button1 = Button(resetax1, 'Reset', hovercolor='0.975')

resetax = fig.add_axes([0.4, 0.025, 0.058, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    a1_slider.reset()
    a2_slider.reset()
    a3_slider.reset()
    a4_slider.reset()

def reset1(event):

    f1_slider.reset()
    f2_slider.reset()
    f3_slider.reset()
    f4_slider.reset()

button.on_clicked(reset)
button1.on_clicked(reset1)

plt.show()
