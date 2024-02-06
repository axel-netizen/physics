import matplotlib.pyplot as plt 

'''
    This code presents the numerical solution to 2 bars or plates with 100 and -100 voltage. The 
    the shape of metallic plates can be changed but for this situation, I'm using two bars
'''

#Initialize V0, the array of size NxN and dV 
dV = 0
n  = 100
V  = np.zeros((n,n)) 

#Metallic plates 
V[20:-20,50]  = -100 
V[20:-20,n-60]= 100 
#print(V)

#Metallic square 1
#V[2:-2,4:-4]  = 10
'''
#Metallic square 2 with a voltage of 10 V and -10 V
V[0,:]   = 10
V[n-1,:] = 10
V[:,0]   = 10
V[:,n-1] = 10

V[5:11,-6] = -10
V[5:11,5]  = -10
V[4, 5:11] = -10
V[-5, 5:11] = -10
'''     


while dV < 60:
    for i in range(1,n-1):
        for j in range(1,n-1):
            V[i,j] = (V[i-1,j] + V[i+1,j] + V[i,j-1] + V[i,j+1]) / 4
    dV += 1
    
plt.contour(V,cmap = 'Blues')
plt.colorbar()

plt.show()

