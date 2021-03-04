#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Input File Description:  Barrier doped AlGaAs/GaAs heterostructure.
# -------------------------------------------------------------------
# ----------------
# GENERAL SETTINGS
# ----------------
# TEMPERATURE
T = 300 #Kelvin

# COMPUTATIONAL SCHEME
# 0: Schrodinger
# 1: Schrodinger + nonparabolicity
# 2: Schrodinger-Poisson
# 3: Schrodinger-Poisson with nonparabolicity
# 4: Schrodinger-Exchange interaction
# 5: Schrodinger-Poisson + Exchange interaction
# 6: Schrodinger-Poisson + Exchange interaction with nonparabolicity
# 7: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson then  poisson and DD)
# 8: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD)
# 9: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD) using Gummel & Newton map
computation_scheme = 9

# QUANTUM
# Total subband number to be calculated for electrons
subnumber_h = 20
subnumber_e = 20
# APPLIED ELECTRIC FIELD
Fapplied = 0.00#/50e-9 # (V/m)
vmax= 1.4
vmin= 0.0
Each_Step=0.2# --------------------------------
# REGIONAL SETTINGS FOR SIMULATION
# --------------------------------

# GRID
# For 1D, z-axis is choosen
gridfactor = 0.5#nm
maxgridpoints = 200000 #for controlling the size
mat_type='Zincblende'
# REGIONS
# Region input is a two-dimensional list input.
# An example:
# Si p-n diode. Firstly lets picturize the regional input.
#         | Thickness (nm) | Material | Alloy fraction | Doping(cm^-3) | n or p type |
# Layer 0 |      250.0     |   Si     |      0         |     1e16      |     n       |
# Layer 1 |      250.0     |   Si     |      0         |     1e16      |     p       |
# To input this list in Gallium, we use lists N:
dopp=5e17
"""
material =[[ 100.0, 'AlGaAs', 0.3, 0.0, dopp, 'p','b'],
            [ 40.0, 'AlGaAs', 0.3, 0.0, dopp, 'p','b'],
            [ 20.0, 'GaAs', 0.0, 0.0, 0.0,'n','w'],
            [ 40.0, 'AlGaAs', 0.3, 0.0, dopp, 'n','b'],
            [ 100.0, 'AlGaAs', 0.3, 0.0, dopp, 'n','b']]
"""
material =[#[ 300.0, 'GaAs', 0.0, 0.0, 5e18, 'p','w'], 
          [ 200.0, 'AlGaAs', 0.3, 0.0, 1e18, 'p','b'],
          [ 30.0, 'GaAs', 0.0, 0.0, 0.0,'n','b'],
          [ 5.0, 'InGaAs', 0.3, 0.0, 0.0, 'n','w'],
          [ 30.0, 'GaAs', 0.0, 0.0, 0.0,'n','b'],
          [ 5.0, 'InGaAs', 0.3, 0.0, 0.0, 'n','w'],  
          [ 30.0, 'GaAs', 0.0, 0.0, 0.0,'n','b'], 
          [ 5.0, 'InGaAs', 0.3, 0.0, 0.0, 'n','w'],
          [ 50.0, 'GaAs', 0.0, 0.0, 1e16, 'n','b'],
          [ 30.0, 'MgO_zb', 0.0, 0.0, 0.0, 'n','b']
          ]

import numpy as np
x_max = sum([layer[0] for layer in material])
def round2int(x):
    return int(x+0.5)
n_max=round2int(x_max/gridfactor)
#----------------------------------------
dop_profile=np.zeros(n_max)
#----------------------------------------
Quantum_Regions=True
Quantum_Regions_boundary=np.zeros((1,2))

Quantum_Regions_boundary[0,0]=180
Quantum_Regions_boundary[0,1]=365
#----------------------------------------
surface=np.zeros(2) 
#----------------------------------------
#This is accourding to interpolated Vegard’s law for quaternary AxB(1-x)CyD(1-y)=InxGa(1-x)AsyP(1-y)
#---------------------
inputfilename = "samples_pn_fcadiz2020.py"
from os import path
if __name__ == "__main__": #this code allows you to run the input file directly
    input_obj = vars()
    import sys
    sys.path.append(path.join(path.dirname(__file__), '..'))
    import aestimo_eh
    aestimo_eh.run_aestimo(input_obj)
