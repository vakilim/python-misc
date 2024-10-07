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
T = 1 # Duration in seconds
N = 1000
f_Ny = (N/T)/2

# Create the x-axis (time) array, evenly spaced over the duration
t = np.linspace(0, T, N)

# Generate the sine wave
#y = np.sin(T*f*t)
y = y0 + A * np.sin(2*np.pi * f * t + phi)

# Perform the FFT
Y = fft(y)
#N = len(Y)  # Number of sample points

# Get the frequency axis
frequencies = fftfreq(N, 1 / (N/T))

# Calculate the magnitude of the FFT
magnitude = np.abs(Y)

# Only plot the positive frequencies (since FFT is symmetric)
frequencies = frequencies[:N // 2]
magnitude = magnitude[:N // 2]

# Save the original sine wave data to a text file
#np.savetxt('sine_wave_data.txt', np.column_stack((t, y)), header='Time\tAmplitude')

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
