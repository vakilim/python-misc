
import os
import math
import re
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from math import sin, cos

def jetSpeed(D_gas, x):
    return 8.35 + (1022) * x

Q_gas = np.array([13.1, 16.3, 19.5]) #np.linspace(15, 50, 10)
Q_liquid = np.array([15, 22.5, 30])
D_gas = 30

x = ( ((Q_gas / D_gas**(2))**(1/2)) / (Q_liquid**(1/4)) )
y = jetSpeed(D_gas, x)

plt.figure()
plt.plot(x, y, 'r.-', markersize = 15)
plt.xlabel("(Q_gas**(1/2)) / (Q_liquid**(1/4))")
plt.ylabel("Jet speed")
plt.title("Gilt für D_gas = 30")
plt.show()
