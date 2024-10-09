#import os
#import math
#import re
import numpy as np
import matplotlib.pyplot as plt

def curve(q):
    return y0+a*np.power(q, -0.4)
    
y0=0
a=100
q = np.linspace(0.01,0.1,100) #start, stop, no. points
I = curve(q) #x,mu,sig

plt.plot(q,I)
np.savetxt("output.dat", np.array([q, I]).T)
plt.show()

