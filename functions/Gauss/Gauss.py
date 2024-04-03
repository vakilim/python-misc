import os
import math
import re
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    #return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    #return np.exp(-((x-mu)**2)/(2*sig**2))
    return y0 + a * 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)
    #return y0+(a-y0)*np.exp(-(x-mu)*(x-mu)/(2*sig*sig))

y0=70
a=16000
x = np.linspace(1,900,500)
y = gaussian(x,393,119.413)

plt.plot(x,y)
plt.show()
np.savetxt("output_Gaussian.dat", np.array([x, y]).T)

print ("FWHM =", 2.35*119.413)
