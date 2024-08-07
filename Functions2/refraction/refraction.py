import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, asin

# Calculate the sheet thickness
def calculate_pathdifference(d, na, nw, alpha):
    
    # Convert theta from degrees to radians
    #alpha_rad = np.deg2rad(alpha_deg)
    
    # Calculate the expression
    L = 2*nw*d*cos(asin(na/nw*sin(alpha)))    
    # L = nw*2*d/cos_alpha_prime - na*2*d*(na/nw)*np.sin(alpha)*np.sin(alpha)/cos_alpha_prime
    return L    

# Calculate the sheet thickness
def calculate_upperlimit(lambda_0, delta_lambda):
    upperlimit = 0.44 * np.power(lambda_0, 2) / delta_lambda
    return upperlimit

# Calculate the L1, L2
def calculate_L1(d, alpha):
    L1 = d/cos(asin((na/nw)*sin(alpha)))
    return L1

# Calculate the L3
def calculate_L3(d, alpha_prime):
    L3 = 2*d*tan(asin((na/nw)*sin(alpha)))*sin(alpha)
    return L3

#add values for the angle and the refractive indeces
d = 1.5 #sheet thickness in um
na = 1.0
nw = 4/3
alpha = 70*np.pi/180  # angle in degrees
#alpha_prime = asin((na/nw)*sin(alpha))
cos_alpha_prime = np.sqrt(1-( ((na/nw)*np.sin(alpha))**2 ))

#light source
lambda_2 = 0.990 #largest wavelength in um
lambda_1 = 0.440 #smallest wavelength in um
lambda_0 = ((lambda_2-lambda_1)/2)+lambda_1 #center wavelength in um
delta_lambda = lambda_2 - lambda_1 #spectral width of the light source

result = calculate_pathdifference(d, na, nw, alpha)
result_2 = calculate_upperlimit(lambda_0, delta_lambda)
result_3 = calculate_L1(d, alpha)
result_4 = calculate_L3(d, alpha)

print("Center wavelength =", lambda_0, "um")
print("Spectral width =", delta_lambda, "um\n")

print("Upper limit in path difference =", result_2, "um\n")

print("L1 = L2 =", result_3, "um")
print("L3 =", result_4, "um")
print("Path difference =", result, "um")
