import os
import math
import re
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from math import sin, cos

def jetSpeed(D_gas, Q_gas, Q_liquid):
    return 6 + (1084/D_gas) * ( (Q_gas**(1/2)) / (Q_liquid**(1/4)) )

### Case 1
D_gas = np.linspace(0, 10, 500)
Q_gas = 38.3
Q_liquid = 10
y = jetSpeed(D_gas, Q_gas, Q_liquid)
np.savetxt("jet_speed_0-1_5_5.dat", np.array([D_gas, y]).T)
plt.figure("case 1")
plt.plot(D_gas, y)

### Case 2
D_gas = 60
Q_gas =  np.linspace(0, 10, 500)
Q_liquid = 10
y = jetSpeed(D_gas, Q_gas, Q_liquid)
np.savetxt("jet_speed_5_0-1_5.dat", np.array([Q_gas, y]).T)
plt.figure("case 2")
plt.plot(Q_gas, y)

### Case 3
D_gas = 60
Q_gas = 38.3
Q_liquid = np.linspace(0, 10, 500)
y = jetSpeed(D_gas, Q_gas, Q_liquid)
np.savetxt("jet_speed_5_5_0-1.dat", np.array([Q_liquid, y]).T)
plt.figure("case 3")
plt.plot(Q_liquid, y)

plt.show()
