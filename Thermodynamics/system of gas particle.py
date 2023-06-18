import matplotlib.pyplot as plt
from scipy.constants import gas_constant
import matplotlib.animation as animation               #importing the modules
import random
from matplotlib.widgets import Slider,RadioButtons,Button

# initializing the constant
NUM_OF_PARTICLES_OPTIONS=[100,200,400]
NUM_OF_PARTICLES=NUM_OF_PARTICLES_OPTIONS[0]
SIZE_OF_CONTAINER=100                  #IN CentiMetre
INITIAL_TEMPERATURE=1
INITAIL_FORCE= 1
Pressure = ((NUM_OF_PARTICLES*gas_constant*INITIAL_TEMPERATURE)/(SIZE_OF_CONTAINER**3))
# random values for all particles
"""here range is NUM_OF_PARTICLES so each particle can be assign a value
 if it is not exactly NUM_OF_PARTICLES then, the problem is not all particle get their value update
  and some particle by default will have zero velocity"""

"""here larger the container higher velocity of particle is required for uniform animatiom when SIZE_OF_CONTAINER is changed"""

positions =[(random.uniform(0,SIZE_OF_CONTAINER),random.uniform(0,SIZE_OF_CONTAINER)) for p in range(NUM_OF_PARTICLES)]
velocities = [(random.uniform(-SIZE_OF_CONTAINER//10,SIZE_OF_CONTAINER//10),random.uniform(-SIZE_OF_CONTAINER//10,SIZE_OF_CONTAINER//10)) for p in range(NUM_OF_PARTICLES)]

#creating plot for fig
fig,ax =plt.subplots()

#adding title
plt.text(0.1,105, 'System of Gas particle ', fontsize=15,bbox = dict(facecolor = 'yellow', alpha = 1))
plt.text(74,113,'Number of Particles',fontsize=10)

"""we want to change the size of container by slider"""
ax.set_xlim(0,SIZE_OF_CONTAINER)              #setting size of container
ax.set_ylim(0,SIZE_OF_CONTAINER)

# plotting a scatter plot for particles
"""here using zip to compress the list into element so the value of list(ie pair of two x and y) 
can be passed into the scatter function; save it is particles variables to update"""
particles = ax.scatter(*zip(*positions))

# creating slider for SIZE OF CONTAINER
container_ax = plt.axes([0.1245,0.01,0.8,0.02])
container_slider = Slider(container_ax,"Container's length (cm)",10,100,valinit=SIZE_OF_CONTAINER,valstep=10)

# creating slider for pressure
force_slider_ax = plt.axes([0.1245,0.05,0.8,0.02])
force_slider= Slider(force_slider_ax,'Force (N)',0.1,5,valinit=1,valstep=0.5)

# creating slider for temperature
temperature_slider_ax = plt.axes([0.1245,0.03,0.8,0.02])
temperature_slider= Slider(temperature_slider_ax,"Temperature (K)",1,300,valinit=51,valstep=50)

# radio button slider
NUM_OF_PARTICLES_Radio_ax = plt.axes([0.7,0.88,0.2,0.1])
NUM_OF_PARTICLES_Radio= RadioButtons(NUM_OF_PARTICLES_Radio_ax, ('100', '200', '400'), active=0,activecolor='skyblue')

# update function for func animation
"""here we want to update the value of each particle to it respective velocity at the same index position on the list"""
def update(frame):

    # getting current temp and pressure from the slider
    INITAIL_FORCE= force_slider.val
    INITIAL_TEMPERATURE= temperature_slider.val
    container = int(container_slider.val)

    # Get the selected number of particles from the radio button
    num_particles = int(NUM_OF_PARTICLES_Radio.value_selected)

    # global function declaration and updating no of particles
    global NUM_OF_PARTICLES, positions, velocities, SIZE_OF_CONTAINER
    if num_particles!=NUM_OF_PARTICLES:
        NUM_OF_PARTICLES=num_particles
        positions = [(random.uniform(0, SIZE_OF_CONTAINER), random.uniform(0, SIZE_OF_CONTAINER)) for p in range(NUM_OF_PARTICLES)]
        velocities = [(random.uniform(-SIZE_OF_CONTAINER // 10, SIZE_OF_CONTAINER // 10),random.uniform(-SIZE_OF_CONTAINER // 10, SIZE_OF_CONTAINER // 10)) for p in range(NUM_OF_PARTICLES)]
    elif container!= SIZE_OF_CONTAINER:
        SIZE_OF_CONTAINER = container
        positions = [(random.uniform(0, SIZE_OF_CONTAINER), random.uniform(0, SIZE_OF_CONTAINER)) for p in range(NUM_OF_PARTICLES)]
        velocities = [(random.uniform(-SIZE_OF_CONTAINER // 10, SIZE_OF_CONTAINER // 10),random.uniform(-SIZE_OF_CONTAINER // 10, SIZE_OF_CONTAINER // 10)) for p in range(NUM_OF_PARTICLES)]
        
    # updating position on pressure and temperature
    for i in range(NUM_OF_PARTICLES):
        x,y =positions[i]
        Vx,Vy =velocities[i]
        x +=Vx*((INITAIL_FORCE)/18)*((INITIAL_TEMPERATURE/100))*(1/(SIZE_OF_CONTAINER/150))
        y +=Vy*((INITAIL_FORCE)/18)*((INITIAL_TEMPERATURE/100))*(1/(SIZE_OF_CONTAINER/150))

        # check for collisions with container walls
        if x<0 or x>SIZE_OF_CONTAINER:
            """if particle collide with container walls then the direction of velocity is reversed in x"""
            Vx = Vx*(-1)
        if y<0 or y>SIZE_OF_CONTAINER:
            """if particle collide with container walls then the direction of velocity is reversed in y"""
            Vy = Vy*(-1)

        """updating the value of particle after change in velocity or prssure or temperature"""
        positions[i] = x,y
        velocities[i] = Vx,Vy

    # updating the scatter plot
    particles.set_offsets(positions)

    return particles,

"""updating value of prssure and temperature when slider value is changed"""
force_slider.on_changed(update)
temperature_slider.on_changed(update)
NUM_OF_PARTICLES_Radio.on_clicked(update)
container_slider.on_changed(update)

# creating animation by func animation
"""fig is the figure containing scatter plot and update is the function returning the updated value of positions"""
ANIMATION =animation.FuncAnimation(fig,update,frames=100,interval=50,blit=True)

# reset button
reset = plt.axes([0.91, 0.1, 0.08, 0.05])
button = Button(reset, 'Reset', color='gold',
                hovercolor='red')

#function to reset
def resetslider(event):
    force_slider.reset()
    container_slider.reset()
    temperature_slider.reset()

'''calling reset slider'''
button.on_clicked(resetslider)


#Display the animation
plt.show()

