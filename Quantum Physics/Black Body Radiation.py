
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider,Button
from scipy.constants import h, c, k
from mpmath import mp


"""intializing Temp in Kelvin"""
T = 7000
G = 5500
L = 3000

"""wein displacement constant"""
b =2898e3

"""wavelength"""
lampeak= b/T            #maximum value of wavelength

"""ceating subplots"""
plt.figure(figsize=(13,6),dpi=100)
ax=plt.subplot()
plt.subplots_adjust(bottom=0.25)

"""labels"""
plt.ylabel("Intensity",fontsize='15')
plt.xlabel("wavelengths (nm)",fontsize='15')


"""setting value of x and y axis"""
wl = np.arange(1e-9,6e-6,1e-8) # x axis

"defining function"
def Intensity(t):
    wl = np.arange(1e-9, 6e-6, 1e-8)
    intensityT = np.zeros_like(wl)
    for i, w in enumerate(wl):
        C = mp.mpf(h * c / (k * t * w))
        intensityT[i] = mp.mpf(2.0 * h * c ** 2) / (w ** 5 * (mp.exp(C) - 1.0))
    return intensityT


"storing value from Intensity functions in new variables"
intensityT = Intensity(T)
intensityL = Intensity(L)
intensityG = Intensity(G)

"""lim and ticks"""
plt.xlim(0,3000)
plt.ylim(0,1.5e14)
plt.xticks(np.arange(0,3000,200))
plt.yticks(np.arange(0,1.5e14,1e13))

"""vertical dashed line"""
plt.vlines(x=380,ymin=0,ymax=5e14,color='black',linestyles='dashed')
plt.vlines(x=750,ymin=0,ymax=5e14,color='black',linestyles='dashed')

"wavelength in nanometer"
x=wl*1e9

"""plot intensityT vs wavelength in nm as a red line"""
t, =plt.plot(x, intensityT, 'k-',lw = 1.5,label='body A')
g, =plt.plot(x, intensityG, 'k-',lw = 1.5,label='body B')
l, =plt.plot(x, intensityL, 'k-',lw = 1.5,label='body C')
plt.legend(borderpad = 0.5, labelspacing = 1.5)

"""text box for wavelength """
text1 =ax.text(2420,14.1e13,f" {round(b/T,)} nm",fontsize=11,bbox=dict(facecolor='skyblue',alpha = 0.5))
text2 =ax.text(2420,12.8e13,f" {round(b/G,)} nm",fontsize=11,bbox=dict(facecolor='skyblue',alpha = 0.5))
text3 =ax.text(2420,11.5e13,f" {round(b/L,)} nm",fontsize=11,bbox=dict(facecolor='skyblue',alpha = 0.5))

'''texts'''
plt.text(470,16e13, 'Visible', fontsize=15,bbox = dict(facecolor = 'yellow', alpha = 0.5))
plt.text(200,16e13, 'UV', fontsize=15)
plt.text(800,16e13, 'Infrared', fontsize=15)
plt.text(2330,15.7e13, 'Wavelenth at peak', fontsize=11,bbox = dict(facecolor = 'white',alpha = 0.5))

"""creating slider"""
axT = plt.axes([0.1,0.095,0.8,0.04])                                  # axis for slider1
sliderT = Slider(axT,'Temp A(K)',1500,8000,valinit=7000,valstep=10)           # creating slider1
axG = plt.axes([0.1,0.05,0.8,0.04])                                   # axis for slider2
sliderG = Slider(axG,'Temp B(K)',1500,8000,valinit=5500,valstep=10)           # creating slider2
axL = plt.axes([0.1,0.01,0.8,0.04])                                   # axis for slider3
sliderL = Slider(axL,'Temp C(K)',1500,8000,valinit=3000,valstep=10)           # creating slider3

"""creating function for slider value update"""
def update(val):
    global text1,text2,text3                                             #gobal variable
    T = sliderT.val
    L = sliderL.val
    G = sliderG.val
    t.set_ydata(Intensity(T))
    l.set_ydata(Intensity(L))
    g.set_ydata(Intensity(G))

    text1.set_visible(False)                                             #to redraw
    text2.set_visible(False)
    text3.set_visible(False)
    text1 = ax.text(2420, 14.1e13, f" {round(b / T, )} nm", fontsize=11, bbox=dict(facecolor='skyblue', alpha=0.5))
    text2 = ax.text(2420, 12.8e13, f" {round(b / G, )} nm", fontsize=11, bbox=dict(facecolor='skyblue', alpha=0.5))
    text3 = ax.text(2420, 11.5e13, f" {round(b / L, )} nm", fontsize=11, bbox=dict(facecolor='skyblue', alpha=0.5))


"""updating value"""
sliderG.on_changed(update)
sliderT.on_changed(update)
sliderL.on_changed(update)

"""reset button"""
reset = plt.axes([0.9, 0.15, 0.05, 0.04])
button = Button(reset, 'Reset', color='gold',
                hovercolor='red')

"""function to reset slider"""
def resetslider(event):
    sliderT.reset()
    sliderG.reset()
    sliderL.reset()

'''calling reset slider'''
button.on_clicked(resetslider)


plt.show()
