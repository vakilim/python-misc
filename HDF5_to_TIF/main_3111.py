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

base_path = "C:/p003111/raw/r{:0>4d}"
base_path_processed = "C:/p003111/processed/r{:0>4d}"
run = 137
input_path = os.path.join(base_path,
'RAW-R{:0>4d}-DA02-S00000.h5').format(run,run)
output_path = os.path.join(base_path_processed,
'RAW-R{:0>4d}-DA02-S00000-2.h5.tiff').format(run,run)

with h5py.File(input_path) as file:
     img = file['/INSTRUMENT/SPB_EXP_ZYLA/CAM/1:daqOutput/data/image/pixels'][33,:,:]

#img = np.array(img.reshape((4, -1)), np.int16)
plt.rcParams["figure.figsize"] = (30,30)
plt.imshow(img)
plt.show()

tiff.imsave(output_path, img)