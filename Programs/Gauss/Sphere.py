#import os
#import math
#import re
import numpy as np
import matplotlib.pyplot as plt

def formfactor(q,r):
    return V * ((3 * (np.sin(A)-A*np.cos(A))) / A**3)**2

def bessel(q,r):
    return (((np.sin(A)-A*np.cos(A))) / A**2)**2


q = np.linspace(0.001, 2, 500) #start, stop, no. points
r = 30 #nm
A = q*r
V = (4/3)*np.pi*(r**3)
y = formfactor(q,r)
z = bessel(q,r)

plt.plot(np.log(q), np.log(y))
plt.xlabel('q [nm^-1]')
plt.ylabel('I(q)')
#plt.xlim(0, 2)
np.savetxt("output_sphere.dat", np.array([q, y]).T)
plt.show()

#q_min = 4.493/r