# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:04:07 2024

@author: vakilim
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the shape (a simple rectangle in this case)
def create_shape():
    shape = np.zeros((256, 256))
    shape[96:160, 96:160] = 1  # A rectangle in the center
    return shape

# Perform the 2D FFT
def compute_fft2(shape):
    fft2_result = np.fft.fftshift(np.fft.fft2(shape))  # Shift the zero-frequency component to the center
    magnitude = np.abs(fft2_result)
    phase = np.angle(fft2_result)
    return fft2_result, magnitude, phase

# Save complex numbers and phases to a CSV file
def save_to_csv(fft2_result, phase, filename):
    complex_numbers = fft2_result.flatten()
    phase_values = phase.flatten()

    # Create a DataFrame
    df = pd.DataFrame({
        'Complex_Number': complex_numbers,
        'Phase': phase_values
    })

    # Save to CSV
    df.to_csv(filename, index=False)

# Plot the original shape and its FFT magnitude
def plot_results(shape, magnitude):
    plt.figure(figsize=(12, 6))

    # Plot the original shape
    plt.subplot(1, 2, 1)
    plt.title("Original Shape")
    plt.imshow(shape, cmap='gray')
    plt.colorbar()

    # Plot the magnitude of the FFT
    plt.subplot(1, 2, 2)
    plt.title("2D FFT Magnitude")
    plt.imshow(np.log(magnitude + 200), cmap='gray')  # Log scale for better visibility
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    # Step 1: Create the shape
    shape = create_shape()

    # Step 2: Perform the 2D FFT
    fft2_result, magnitude, phase = compute_fft2(shape)

    # Step 3: Save results to CSV (complex numbers and phases)
    save_to_csv(fft2_result, phase, 'fft2_results.csv')

    # Step 4: Plot the results
    plot_results(shape, magnitude)

    print("2D FFT saved to 'fft2_results.csv' and results plotted.")
