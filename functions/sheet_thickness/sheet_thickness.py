import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
# Read the CSV file
df = pd.read_csv('Si_5s_LED.csv', skiprows=53)
print(df.head())

# Extracting data from CSV columns
wavelength = df.iloc[:, 0]
intensity = df.iloc[:, 1]
"""

"""
# Plot original data
plt.figure(figsize=(10, 6))
plt.plot(wavelength, intensity, label='Original Data')
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Intensity vs Wavelength')
plt.legend()
plt.show()
"""

# Calculate the custom formula
def calculate_thickness(n1, n2, lambda1,lambda2, theta_deg):
   
    # Convert theta from degrees to radians
    theta_rad = np.deg2rad(theta_deg)
 
    # Calculate the expression    
    thickness = (((2 * (n1**2 - (np.sin(theta_rad)**2))**(1/2)) / lambda1) - 
                (((2 * (n2**2 - (np.sin(theta_rad)**2))**(1/2)) / lambda2)))**-1
   
    return thickness

n1 = 1.7942 #ref. index 1, 4.088
lambda1 = 449.35 #wavelength 1, 549.6
n2 = 1.7452 #ref. index 2, 3.770
lambda2 = 610.86 #wavelength 2, 713.5
theta = 45  # angle in degrees

result = calculate_thickness(n1, n2, lambda1, lambda2, theta)
print("Thickness =", result, "nm")
