import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks #savgol_filter
from scipy.ndimage import gaussian_filter1d

#os.chdir('C:\\Git\\python-misc\\functions\\peak_detection\\CSVs')

# Read the CSV file
df = pd.read_csv('C:\\Git\python-misc\\programs\\peak_detection\\CSVs\\water_sheet_200_10s.csv', skiprows=53, nrows=3645)

#print(df.head(3))
#print(df.tail(3))

# Assign column names
df.columns = ['wavelength', 'intensity']

print( df.dtypes)

print("\n", type(df['wavelength']))

"""
# Create a new column by copying values of the wavelength column
df['wavelength_copy'] = (df['wavelength'])
"""

# Extracting data from CSV columns
wavelength = df.iloc[:, 0].values #first column
intensity = df.iloc[:, 1].values #third column

print(type(wavelength))

"""
#turn values into a one-dimensional numpy array
Wavelength = np.array(df.iloc[:, 0])
print(type(Wavelength))
"""

#df.to_csv("df_output.csv")

# Smooth the intensity data using a Gaussian filter
smoothed_intensity = gaussian_filter1d(intensity, sigma=5)

# Plot the original and smoothed data

plt.figure(figsize=(10, 6))
ax = plt.axes()
ax.set_xlim([300,1000])
ax.set_ylim([-0.001, 0.5])
#ax.set_xticks([])
#ax.set_yticks([])
plt.plot(wavelength, intensity, label='Original Data', color='blue')
plt.plot(wavelength, smoothed_intensity, label='Smoothed Data', color='red')
plt.legend()
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('')
#plt.xticks(np.arange(0, len(wavelength), step=1000),rotation=0)
#plt.xticks(rotation=90)
plt.savefig('title.png', format='png', dpi=300)
plt.show()

# Find peaks in the smoothed_intensity data
peaks, _ = find_peaks(smoothed_intensity, height=0.001, width=0.2, distance=40)

# Plot the smoothed_intensity data with indicated peaks
plt.figure(figsize=(10, 6))
ax = plt.axes()
ax.set_xlim([300,1000])
ax.set_ylim([-0.001, 0.5])
#ax.set_xticks([])
#ax.set_yticks([])
plt.plot(wavelength, smoothed_intensity, label='Smoothed Data', color='red')
plt.plot(wavelength[peaks], smoothed_intensity[peaks], 'x', label='Peaks', color='green', markersize=10)
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Smoothed Data with Peaks')
#plt.xticks(np.arange(0, len(wavelength), step=1000),rotation=0)
plt.legend()
plt.show()

# Print peak positions (wavelength values)
print("Peak Positions (Wavelength values):")

for peak in peaks:
    print(wavelength[peak])

print(len(peaks))