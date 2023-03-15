# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:09:51 2022

@author: etienne
"""


import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import glob
import re
import pandas as pd
##

filename = 'driver_EX1'

if not os.path.exists('outputFiles'):
   os.makedirs('outputFiles')
   
   
# %%

os.system(r'.\bin\AeroDyn_Driver_x64 ' + filename + '.dvr')      #Execute the AeroDyn driver

# %%
# Moves the output files into the correct folder
sourcepath = os.getcwd()
target_folder = r'./outputFiles'
sourcefiles = '*.out'
filelist=glob.glob(sourcefiles)
for single_file in filelist:
    shutil.move(os.path.join(sourcepath, single_file), os.path.join(target_folder, single_file))
# %%

# Number of cases simulated
filelist=glob.glob(target_folder + '/' + sourcefiles)
NumCases=len(filelist)   

# Preallocation
TSR_curve=np.zeros([NumCases])    
Cp_curve=np.zeros([NumCases])
Ct_curve=np.zeros([NumCases])
thrust_curve=np.zeros([NumCases])
speed_curve=np.zeros([NumCases])
wndspeed=np.zeros([NumCases])
power_curve=np.zeros([NumCases])

for i in range (NumCases):
    
    myFile = r'./outputFiles/' + filename + '.'+ str(i+1) + '.out'
    
    
    # Read wind speed
    s =  pd.read_csv(myFile, skiprows=3, nrows=2)
    a = (re.findall( r'\d+\.*\d*', str(s.head())))
    wndspeed[i] = float(a[1])
    
    
    # Read outputs
    s =  pd.read_csv(myFile, header=5, sep='\s+')
    outputfile = np.array(s)
    time= outputfile[:,0]
    ind = np.argmin(np.abs(time-8)) # read only the last 2 seconds
    
    speed_curve[i]= np.mean(outputfile[ind:-1,1])
    TSR_curve[i]= np.mean(outputfile[ind:-1,2])
    power_curve[i]= np.mean(outputfile[ind:-1,3])
    thrust_curve[i]= np.mean(outputfile[ind:-1,4])
    Cp_curve[i]= np.mean(outputfile[ind:-1,5])
    Ct_curve[i]= np.mean(outputfile[ind:-1,6])
    
    

    

#%%

 # short test: plt.plot(wndspeed,power_curve)
