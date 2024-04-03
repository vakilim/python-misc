import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
arr = [[-2,0.625], #function with 14 value pairs, y-intercept is 0.625
[0.10,0.59],
[2.75,0.455],
[4.45,0.2908],
[4.650,0.287],] #end of curve
arr = np.array(arr)
x,y = arr.T
spl = interp.splrep(x,y)
new_x = np.linspace(0, 4.650, 1000) #start, end, no. of lines
ynew = interp.splev(new_x, spl)
np.savetxt("output_500um_3.dat", np.array([new_x, ynew]).T)
plt.plot(new_x, ynew)
plt.show()