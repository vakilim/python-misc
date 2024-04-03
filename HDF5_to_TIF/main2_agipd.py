# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:37:16 2020

@author: vakilim
"""
import os
import h5py
import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt

base_path = "D:/p002695/raw/r{:0>4d}"
base_path_processed = "D:/p002695/processed/r{:0>4d}"
run = 30
input_path = os.path.join(base_path,
'RAW-R{:0>4d}-AGIPD00-S00000.h5').format(run,run)
output_path = os.path.join(base_path_processed,
'RAW-R{:0>4d}-AGIPD00-S00000.h5.tiff').format(run,run)

with h5py.File(input_path) as file:
     img = file['/INSTRUMENT/SPB_DET_AGIPD1M-1/DET/0CH0:xtdf/image/'][2,:,:]

#img = np.array(img.reshape((4, -1)), np.int16)
plt.rcParams["figure.figsize"] = (30,30)
plt.imshow(img)
plt.show()

tiff.imsave(output_path, img)