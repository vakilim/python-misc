import os
#import math
#import re
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    #return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    #return np.exp(-((x-mu)**2)/(2*sig**2))
    return y0+(a-y0) * 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)
    #return y0+(a-y0)*np.exp(-(x-mu)*(x-mu)/(2*sig*sig))

y0=0
a=200
x = np.linspace(1,800,500)
y = gaussian(x,400,180) #x,mu,sig

plt.plot(x,y)
plt.show()
#np.savetxt("output_Gaussian.dat", np.array([x, y]).T)

"""

def test(x):
	y=x**2
	return y
"""

def FWHM(x, y):

    half_max = np.max(y) / 2
    # Find the indices where the y value is closest to half_max
    idx = np.argwhere(np.diff(np.sign(y - half_max))).flatten()
    # Interpolate to find the x values corresponding to half_max
    if len(idx) == 2:
        x1, x2 = x[idx[0]], x[idx[1]]
        return np.abs(x2 - x1)
    else:
        return None

print("FWHM =", FWHM(x, y))




    