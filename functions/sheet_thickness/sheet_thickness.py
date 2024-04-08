import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Calculate the sheet thickness
def calculate_thickness(n1, n2, lambda1,lambda2, theta_deg):
   
    # Convert theta from degrees to radians
    theta_rad = np.deg2rad(theta_deg)
 
    # Calculate the expression    
    
    
    thickness = (((2 * (n1**2 - (np.sin(theta_rad)**2))**(1/2)) / lambda1) - 
                (((2 * (n2**2 - (np.sin(theta_rad)**2))**(1/2)) / lambda2)))**-1
   
    return thickness

#add values for the wavelength and the refractive index
lambda1 = 5.46E+02
lambda2 = 6.11E+02
n1 = 1.3845
n2 = 1.3822
theta = 45  # angle in degrees

result = calculate_thickness(n1, n2, lambda1, lambda2, theta)
print("Thickness =", result, "nm")