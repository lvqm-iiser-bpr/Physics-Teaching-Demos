import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Slider
"function to approximate is cos(x)"

"we are creating a function to estimate the value of cos(x) based on the number of terms"
"x = angles, n = number of terms"
def function_sine(x, n):
     sin_approx = 0                  #final estimation terms
     for i in range(n):
         coefficient = (-1) ** i
         numerator = x ** ((2 * i)+1)
         denominator = math.factorial((2 * i)+1)
         sin_approx += (coefficient) * ((numerator) / (denominator))

     return sin_approx

"selecting the number of terms"
num_terms=0


"axis values"
angles = np.arange(-2 * np.pi,2 * np.pi,0.1)
y_cos= np.sin(angles)
f_cos= [function_sine(angle,num_terms) for angle in angles]

"creating figure"
fig,ax = plt.subplots(figsize=(12,6))

"plotting the curve of cos"
ax.plot(angles,y_cos,label='sin(x)')

"plotting the curve for the estimated value of cosx"
ax.plot(angles,f_cos,label ='Taylor Series Approximation ({} terms)'.format(num_terms))

"putting limit,legend,grid and title"
ax.set_ylim(-2,2)
ax.legend()
plt.suptitle('Taylor series for Sin(x)',bbox= dict(facecolor = 'yellow',alpha = 0.5))
plt.grid(True)

"slider"
sliderax=plt.axes([0.3,0.01,0.44,0.03])
slider = Slider(sliderax,"Numbers of terms",0,10,valinit=0,valstep=1)

def update(val):
    global num_terms
    s = slider.val
    num_terms = s
    f_cos = [function_sine(angle, num_terms) for angle in angles]
    ax.cla()
    ax.plot(angles, y_cos, label='sin(x)')
    ax.plot(angles, f_cos, label='Taylor Series Approximation ({} terms)'.format(num_terms))
    ax.set_ylim(-2, 2)
    ax.legend()
    ax.grid(True)

slider.on_changed(update)

plt.show()
