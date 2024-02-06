import matplotlib.pyplot as plt 
import numpy as np

n =  2000
t =  np.zeros(n)
v =  np.zeros(n)
vd = np.zeros(n)

m = 70
P = 400
dt = 0.1

v[0]  = 4
vd[0] = 4
t[0]  = 0
C = 0.5
A = 0.33
rho = 1.2

for i in range(n-1):
    v[i+1]  = v[i] + (P/(m*v[i])) * dt 
    vd[i+1] = vd[i] + (P/(m*vd[i])) * dt - ((C*rho*A*(vd[i])**2) / (2*m)) * dt 
    t[i+1]  = t[i] + dt 

plt.plot(t,v) 
plt.plot(t,vd) 
plt.pause(0.01)
plt.show()

