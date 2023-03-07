# aerodyn_ENERGI210

## Summary
Minimalistic exercise on the blade element momentum (BEM) theory with the software Aerodyn for teaching in the course [ENERGI210](https://www.uib.no/en/course/ENERGI210) at the University of Bergen (UiB)

## Content

The repository contains:
  - **driver_EX1.dvr** as the .dvr file used for the tutorial
  - **Ex1_input.dat** as input
  - **NRELOffshrBsline5MW_AeroDyn_blade.dat** as input
  - The script **RUN_ME.m** which calls Aerodyn and processes some of the output data
  - The folder **functions**, which contains the functions used in RUN_ME.m
  - A folder **bin** containing various versions of Aerodyn.exe
  - A folder **airfoil_NREL_5MW**, which contains the airfoil data for the 5 MW NREL turbine
  
 For those who prefer python, it is possible to use **RUN_ME.py** on Windows. However, this script is less robust than the Matlab version
  
  The first time that RUN_ME is used, a folder **outputFiles** is created. The output files are stored in this folder automatically
 
