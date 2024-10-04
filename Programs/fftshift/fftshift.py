# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:13:12 2024

@author: vakilim
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to create a sine wave and return x, y values
def create_sine_wave(y0, A, f, phi, num_points=1000):
    # Create the x-axis values spanning from 0 to 2π
    x = np.linspace(0, 2 * np.pi, num_points)
    
    # Calculate the y-axis values according to the sine function
    y = y0 + A * np.sin(f * x + phi)
    
    return x, y

# Function to perform FFT and FFT shift
def perform_fft_shift(y):
    # Perform the FFT
    fft_result = np.fft.fft(y)
    
    # FFT shift: Shift the zero-frequency component to the center
    fft_shifted = np.fft.fftshift(fft_result)
    
    # Calculate the frequencies corresponding to the FFT bins
    freqs = np.fft.fftfreq(len(y))
    freqs_shifted = np.fft.fftshift(freqs)
    
    return freqs_shifted, np.abs(fft_shifted)

# Main function
def main():
    # Parameters for the sine wave
    y0 = 0     # Baseline
    A = 1      # Amplitude
    f = 10     # Frequency (in cycles per 2π)
    phi = 0    # Phase shift
    
    # Generate sine wave
    x, y = create_sine_wave(y0, A, f, phi)
    
    # Perform FFT and FFT shift
    freqs_shifted, fft_shifted = perform_fft_shift(y)
    
    # Plot the sine wave
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.title('Sine Wave: $y = y_0 + A \cdot \sin(f \cdot x + \phi)$')
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    
    # Plot the FFT-shifted result
    plt.subplot(1, 2, 2)
    plt.plot(freqs_shifted, fft_shifted)
    plt.title('FFT Shift of Sine Wave')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    
    # Show the plots
    plt.tight_layout()
    plt.show()
    #np.savetxt("output.dat", np.array([x, y]).T)

# Call the main function
if __name__ == "__main__":
    main()
