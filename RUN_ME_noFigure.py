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
##

filename = 'driver_EX1'

# %%
os.system('bin/AeroDyn_Driver_x64 ' + filename + '.dvr')      #Execute the AeroDyn driver

# Moves the output files into the correct folder
sourcepath = os.getcwd()
target_folder = './outputFiles'
sourcefiles = '*.out'
filelist=glob.glob(sourcefiles)
for single_file in filelist:
    shutil.move(os.path.join(sourcepath, single_file), os.path.join(target_folder, single_file))
# %%

# Number of cases simulated
NumCases=len(filelist)   

# Preallocation
TSR_curve=[0]*NumCases      
Cp_curve=[0]*NumCases
Ct_curve=[0]*NumCases
thrust_curve=[0]*NumCases
speed_curve=[0]*NumCases
wndspeed=[0]*NumCases
power_curve=[0]*NumCases

for i in range (1,NumCases):
    
    
    outputfile= np.loadtxt('./outputFiles/'+filename + '.'+ str(i) + '.out',
                           skiprows=4, max_rows = 1,unpack=True, delimiter=';',
                           dtype={'names': ('case', 'wndspeed'),'formats': ('|S25', '|S15')})
                   
    
    a = outputfile[0].tostring()
    a = a.decode('utf-8')     
    a = (re.findall( r'\d+\.*\d*', a))
    wndspeed[i] = float(a[1])
    
    outputfile= np.loadtxt('./outputFiles/'+filename + '.'+ str(i) + '.out',  skiprows=9, 
                       unpack=True, 
                       dtype={'names': ('time', 'speed', 'TSR','power', 'thrust', 'Cp', 'Ct'),
                              'formats': ('f8', 'f8', 'f8', 'f8', 'f8', 'f8' ,'f8')})
    
    

    time= np.array(outputfile[0], copy=True)
    speed= np.array(outputfile[1], copy=True)
    TSR= np.array(outputfile[2], copy=True)
    power= np.array(outputfile[3], copy=True)
    thrust= np.array(outputfile[4], copy=True)
    Cp= np.array(outputfile[5], copy=True)
    Ct= np.array(outputfile[6], copy=True)

    TSR_curve[i] = np.mean(TSR)         #Save the mean values at each case number in an array
    Cp_curve[i] = np.mean(Cp)
    Ct_curve[i] = np.mean(Ct)
    thrust_curve[i] = np.mean(thrust)
    speed_curve[i] = np.mean(speed)
    power_curve[i] = np.mean(power)

#Remove the zeros in the first position on each array
TSR_curve.remove(0)     
Cp_curve.remove(0)
Ct_curve.remove(0)   
thrust_curve.remove(0)   
speed_curve.remove(0)
wndspeed.remove(0) 
power_curve.remove(0) 
#%%
