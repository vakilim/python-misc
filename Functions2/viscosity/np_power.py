import numpy as np
import matplotlib.pyplot as plt

def v (k):
    return -37.104 * np.power(k, 6) + 147.07 * k**5 - 236.71 * np.power(k, 4) + 195.39 * np.power(k, 3) - 83.745 * np.power(k, 2) + 14.676 * np.power(k, 1) + 0.8914

x = np.linspace(0, 1, 500)
y = v(x)

plt.plot(x, y)
plt.show()
#np.savetxt("output.dat", np.array([x, y]).T)
