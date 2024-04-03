import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
arr = [[-2,0.59], #function with 14 value pairs, y-intercept is 0.59
[0.25991,0.58933],
[0.77027,0.57084],
[1.8809 ,0.49929],
[2.28817,0.45474],
[2.6736,0.39644],
[3.05588,0.33167],
[3.39887,0.26959],
[3.75636,0.21095],
[4.06532,0.16324],
[4.48594,0.10635],
[4.80746,0.07666],
[5.1063,0.05831],
[5.35,0.05]] #end of curve
arr = np.array(arr)
x,y = arr.T
spl = interp.splrep(x,y)
new_x = np.linspace(0, 5.350, 1000) #start, end, no. of lines
ynew = interp.splev(new_x, spl)
np.savetxt("output.dat", np.array([new_x, ynew]).T)
plt.plot(new_x, ynew)
plt.show()