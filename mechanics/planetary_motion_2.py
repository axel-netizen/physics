from math import *
import matplotlib.pyplot as plt

"""
    This program shows the orbit of two body system. This can be used for 
    simulate the motion of planets.

    We need the following initial conditions: 

    initial displacement in [x] and [y]
    intial velocities [vx] and [vy] 
    time [t] and timesteps [dt] 

    Then we apply the Euler-Cromer method to obtain the numerical solutions. 
    Finally, the results obtained are ploted.
"""

#Initial position
x  = 1 ; y  = 0 
#Initial velocity
vx = 0 ; vy = 2 * pi
#Initial time and timestep  
t = 0  ; dt = 0.01 

xresult = []
yresult = []

while t <= 1.1:
    r  = sqrt(x**2 + y**2)
    vx -= (( 4 * pi**2 * x ) / r**3 ) * dt 
    vy -= (( 4 * pi**2 * y ) / r**3 ) * dt
    x  += vx * dt 
    y  += vy * dt 
    t  += dt  

    xresult.append(x)
    yresult.append(y)

    plt.plot(xresult,yresult)
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    plt.pause(0.1)

plt.show()


