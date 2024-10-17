# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:08:52 2024

@author: vakilim
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# Define sine wave parameters
y0 = 0 # Baseline offset
A = 1 # Amplitude
f = 10 # Frequency in Hz, cycles per second
phi = 0 # Phase shift
T = 1# Duration in seconds
N = 1000 # Number of sample points
f_Ny = (N/T)/2
delta_t = T/N

# Create the x-axis (time) array, evenly spaced over the duration
t = np.linspace(0, T, N)

# Generate the sine wave
#y = np.sin(T*f*t)
y = y0 + A * np.sin(2*np.pi * f * t + phi) #+ np.sin(2*np.pi * 100 * t + phi)

# Perform the FFT
Y = fft(y)

# Get the frequency axis
frequencies = fftfreq(N, delta_t)

# Calculate the magnitude of the FFT
magnitude = np.abs(Y)

# Only plot the positive frequencies (since FFT is symmetric)
frequencies = frequencies#[:N // 2]
magnitude = magnitude#[:N // 2]

# Save the original sine wave data to a text file
#np.savetxt('sine_data.txt', np.column_stack((t, y)), header='Duration\tAmplitude')

# Save the FFT result (frequency and magnitude) to a text file
#np.savetxt('fft_data.txt', np.column_stack((frequencies, magnitude)), header='Frequency\tMagnitude')

# Plot the original sine wave
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.title('Original Sine Wave')
plt.xlabel('Duration [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the magnitude of the FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('FFT Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

#Sig=Re+j*Im
#Phi=np.arctan(Im/Re)
#Mag=np.sqrt((Re**2)+(Im**2))

max_index = np.argmax(np.abs(Y)) # Find the index of the maximum Y-value
print(frequencies[max_index]) # Print the index of the x-axis value where the maximum occurs