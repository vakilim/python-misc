#%matplotlib notebook
import os
import math
import re
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from math import sin, cos

def jetSpeed(D_gas, x):
    return 6 + (1084/D_gas) * x

Q_gas = np.array([5, 10, 15]) #np.linspace(15, 50, 10)
Q_liquid = np.array([15, 35, 45])
D_gas = 60

Q_gas_XX, Q_liquid_YY = np.meshgrid(np.linspace(5, 10, 50), np.linspace(5, 10, 50))

x = ( (Q_gas_XX**(1/2)) / (Q_liquid_YY**(1/4)) )
y = jetSpeed(D_gas, x)

plt.figure()
plt.pcolormesh(y)
plt.colorbar()
plt.xlabel("Q_liquid [µL/min]")
plt.ylabel("Q_gas [mg/min]")
plt.title("For D_gas = 60 µm")
plt.show()