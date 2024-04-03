import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
arr = [[-2,0.625], #function with 14 value pairs, y-intercept is 0.625
[0.10,0.59],
[0.8,0.570],
[2.2,0.49],
[2.75,0.45],
[5.35,0.251],
[5.45,0.2508],
[5.555,0.2504],
[5.650,0.25],] #end of curve
arr = np.array(arr)
x,y = arr.T
spl = interp.splrep(x,y)
new_x = np.linspace(0, 5.650, 1220) #start, end, no. of lines
ynew = interp.splev(new_x, spl)
np.savetxt("output_500um_2.dat", np.array([new_x, ynew]).T)
plt.plot(new_x, ynew)
plt.show()