import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
arr = [[-2,0.4], #function with value pairs, y-intercept is 0.59
[4.65,0.251],
[4.66,0.252],
[5.65,0.0125]] #end of curve
arr = np.array(arr)
x,y = arr.T
spl = interp.splrep(x,y)
new_x = np.linspace(4.65, 5.65, 1000) #start, end, no. of lines
ynew = interp.splev(new_x, spl)
np.savetxt("output_25um_2.dat", np.array([new_x, ynew]).T)
plt.plot(new_x, ynew)
plt.show()