import numpy as np
from math import sin

# Calculate the sheet thickness
def calculate_thickness(m, n, lambda1, lambda2, theta_rad):

    # Calculate the expression    
    thickness = m/b*c
   
    return thickness

#add values for the wavelength and the refractive index
lambda_1 = 410 #smallest wavelength in nm
lambda_2 = 745 #largest wavelength in nm
delta_lambda = lambda_1 - lambda_2

m = 2 #number of peaks in wavelength range
n = 1.33 #ref. index water
theta_deg = 45  # angle in degrees
theta_rad = np.deg2rad(theta_deg)
b = 2*np.sqrt(n**2-(np.sin(theta_rad))**2)
c = ((lambda_1**-1)-(lambda_2**-1))**-1

result = calculate_thickness(m, n, lambda_1, lambda_2, theta_rad)
print("Thickness =", result, "nm")

#lambda_2 = 410 #smallest wavelength in nm
#lambda_1 = 745 #largest wavelength in nm

#lambda_2 = 360 #smallest wavelength in nm
#lambda_1 = 2600 #largest wavelength in nm
