import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks #savgol_filter
from scipy.ndimage import gaussian_filter1d

#os.chdir('C:\\Git\\python-misc\\functions\\peak_detection\\CSVs')
# Read the CSV file
df = pd.read_csv('C:\\Git\\python-misc\\functions\\peak_detection\\CSVs\\SiN_100nm_10s_LED2.csv', skiprows=53)

print(df.head())

# Rename columns
df.columns = ['wavelength', 'intensity']

print(type(df['wavelength']))

print("\n", df.dtypes)

# Create a new column by copying values of the wavelength column
#df['wavelength_copy'] = (df['wavelength'])

# Extracting data from CSV columns
wavelength = df.iloc[:, 0].values #first column
intensity = df.iloc[:, 1].values #third column

print(type(wavelength))

#df.to_csv("df_output.csv")

# Smooth the intensity data using a Gaussian filter
smoothed_intensity = gaussian_filter1d(intensity, sigma=10)

# Plot the original and smoothed data
plt.figure(figsize=(10, 6))
plt.plot(wavelength, intensity, label='Original Data', color='blue')
plt.plot(wavelength, smoothed_intensity, label='Smoothed Data', color='red')
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Original and Smoothed Data')
plt.xticks(np.arange(0, len(wavelength), step=1000),rotation=0)
#plt.xticks(rotation=90)
plt.legend()
plt.show()

# Find peaks in the smoothed_intensity data
peaks, _ = find_peaks(smoothed_intensity, height=0.005, width=30, distance=100)

# Plot the smoothed_intensity data with indicated peaks
plt.figure(figsize=(10, 6))
plt.plot(wavelength, smoothed_intensity, label='Smoothed Data', color='red')
plt.plot(wavelength[peaks], smoothed_intensity[peaks], 'x', label='Peaks', color='green', markersize=10)
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Smoothed Data with Peaks')
plt.xticks(np.arange(0, len(wavelength), step=1000),rotation=0)
plt.legend()
plt.show()

# Print peak positions (wavelength values)
print("Peak Positions (Wavelength values):")

for peak in peaks:
    print(wavelength[peak])