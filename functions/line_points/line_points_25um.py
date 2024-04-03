import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
arr = [[-2,0.59], #function with value pairs, y-intercept is 0.59
[0.25991,0.58933],
[0.77027,0.57084],
[2.6736,0.39644],
[3.05588,0.33167],
[5.35,0.0125]] #end of curve
arr = np.array(arr)
x,y = arr.T
spl = interp.splrep(x,y)
new_x = np.linspace(0, 5.350, 1200) #start, end, no. of lines
ynew = interp.splev(new_x, spl)
np.savetxt("output_25um.dat", np.array([new_x, ynew]).T)
plt.plot(new_x, ynew)
plt.show()