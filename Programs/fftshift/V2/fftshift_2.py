# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
N = 1000  # Number of points
y0 = 0  # Baseline value
A = 1  # Amplitude
f = 10 # Frequency (in Hz or cycles per 2π)
omega = 2*np.pi*f
phi = 0  # Phase shift (in radians)
T = 2*np.pi # Period in rad
f_Ny = (N/T)/2
delta_t = T/N

# Generate the x-axis from 0 to 2π
t = np.linspace(0, T, N)

# Generate the sine wave using the equation y = y0 + A * sin(f * x + phi)
y = y0 + A * np.sin(omega*t + phi)

# Perform FFT
y_fft = np.fft.fft(y)

# Perform FFT Shift
y_fft_shifted = np.fft.fftshift(y_fft)

# Compute the frequency axis for plotting FFT
frequencies = np.fft.fftfreq(N, delta_t)
frequencies_shifted = np.fft.fftshift(frequencies)

# Plot the original sine wave
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, y)
#plt.xlim(0, T)
plt.title('Original Sine Wave')
plt.xlabel('t (radians)')
plt.ylabel('Amplitude')

# Plot the magnitude of the FFT (shifted)
plt.subplot(2, 1, 2)
plt.plot(frequencies_shifted, np.abs(y_fft_shifted))
plt.title('FFT of the Sine Wave (Shifted)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

# Save the original curve data to a text file
#np.savetxt('sine_wave.txt', np.column_stack((x, y)), header='x, Amplitude', comments='')

# Save the FFT (shifted) data to a text file
#np.savetxt('fft_shifted.txt', np.column_stack((frequencies_shifted, np.abs(y_fft_shifted))), header='frequency, magnitude', comments='')

max_index = np.argmax(np.abs(y_fft)) # Find the index of the maximum Y-value
print(frequencies[max_index]) # Print the index of the x-axis value where the maximum occurs