import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.gridspec as gridspec #import gridspec to specify the geometry of the grid to place a subplot
fig=plt.figure() #make a figure to add subplots in it
gs=gridspec.GridSpec(4,1) #add grid for subpolts with 4 rows 1 columns
fig.suptitle('INTERFERENCE', fontsize=16,color='black') #title for the plot
plt.subplots_adjust(bottom=0.3,wspace =0.3,hspace=1)  # wspace=width between subplots , hspace=height distance between subplots

x = np.arange(0,10,0.1) #value of x axis
δ= 0
ares = np.sqrt(10*10+10*10 + (2 * 10 * 10 * np.cos(δ)))
y = 10*np.sin(np.pi*x+0) # equation of 1st wave
y2 = 10*np.sin(np.pi*x+0) # equation of 2nd wave
y3 = ares*(np.sin(np.pi * x + 0))#equation of 3rd wave

u = fig.add_subplot(gs[2,0]) #add first subplot at bottom left (wave1)
uu,=u.plot(x,y,color='red')
u.set_ylim(-15,15)

u2=fig.add_subplot(gs[3,0])  #add 2nd subplot bottom right wave 2
uu2,=u2.plot(x,y2,color='blue')
u2.set_ylim(-15,15)

u3=fig.add_subplot(gs[:2,0])  #add 3rd subplot bottom right wave resultant
uu3,= u3.plot(x,y3,color='green')
u3.set_ylim(-25,25)

#titles
u.set_title('WAVE1',color='red')
u2.set_title('WAVE2',color='blue')

#ylabels
u.set_ylabel("y1") #y axis label
u2.set_ylabel("y2")
u3.set_ylabel("y(resultant)")
#xlabels
u3.set_xlabel("x")

p=0
p2=0
θ=0


#axes for sliders
px = plt.axes([0.4,0.35,0.2,0.01])
p2x=plt.axes([0.4,0.15,0.2,0.01])
# slider
phi = Slider(px,'',0,2*np.pi,valinit=0) #defining sliders
phi2=Slider(p2x,'',0,2*np.pi,valinit=0)
text1 = u.text(6.4, -30, f"Φ1 = {p/np.pi} π")
text2 = u2.text(6.4, -30, f"Φ2 = {p2/np.pi} π")
text3 = u3.text(3.6, 30, f"Resultant wave equation  y= {round(ares,2)}sin(πx+{round(θ,2)})")
text4 = u.text(5.3, 18.5, f"y= 10sin(πx+{p/np.pi}π)")
text5 = u2.text(5.3, 18.5, f"y= 10sin(πx+{p2/np.pi}π)")
text6= u2.text(-0.45,-43,f"A1sin(δ)")
text8= u2.text(-0.65,-45,f"-------------------")
text7= u2.text(-0.65,-49,f"A1 + A2 cos(δ)")
text6= u2.text(-1.4,-57,r"Amplitude=$\sqrt{A₁²,+A₂²+2A₁A₂cosδ}$")
text9= u2.text(-1.25,-45,f"tan(θ)=")
text10 = u2.text(-1,-38.5,f"δ=Φ2-Φ1")
u.grid(True) #making grids inside subplots
u2.grid(True)
u3.grid(True)

# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.2,
                    right=0.9,
                    top=0.9,
                    wspace=0.6,
                    hspace=1)
#hiding the default display of slider value
phi.valtext.set_visible(False)
phi2.valtext.set_visible(False)
#defining function to input in slider.onchanged() function
def update(val): #function to be called upon changing the sliders
    global text1 #making variables global so that it can be used inside this function
    global text2
    global text3
    global text4
    global text5
    global p
    global p2
    p = phi.val #p changes the value as phi slider changes the value
    p2 = phi2.val #p2 changes the value as phi2 changes the value
    δ = (p2- p)  #phase difference which changes as p1 and p2 changes
    θ = np.arctan((10 * np.sin(δ)) /(10 + (10 * np.cos(δ))))  # resultant phase
    ares = np.sqrt(10*10+10*10 + (2 * 10 * 10 * np.cos(δ)))  # resultant amplitude equations
    uu.set_ydata(10 * (np.sin(np.pi * x + p)))  # changing the y value as per the slider changes
    uu2.set_ydata(10 * (np.sin(np.pi * x + p2)))
    uu3.set_ydata(ares * (np.sin(np.pi * x + θ)))
    # everytime the function runs and gives the value to all of the variables this will remove the previous assigned value of that variable to avoid its overlapping with newly assigned one
    text1.set_visible(False)
    text2.set_visible(False)
    text3.set_visible(False)
    text4.set_visible(False)
    text5.set_visible(False)
    #updating the initially defined variables (texts) everytime slider value gets updated
    #updating the initially defined variables (texts) everytime slider value gets updated
    text1 = u.text(6.4, -30, f"Φ1 = {round(p / np.pi,3)} π")
    text2 = u2.text(6.4, -30, f"Φ2 = {round(p2 / np.pi,3)} π")
    text3 = u3.text(3.6, 30, f"Resultant wave equation  y= {round(ares, 2)}sin(πx+{round(θ, 2)})")
    text4 = u.text(5.3, 18.5, f"y= 10sin(πx+{round(p / np.pi,3)}π)")
    text5 = u2.text(5.3, 18.5, f"y= 10sin(πx+{round(p2 / np.pi,3)}π)")

#calling functions on changing slider
phi.on_changed(update)
phi2.on_changed(update)




plt.show()
