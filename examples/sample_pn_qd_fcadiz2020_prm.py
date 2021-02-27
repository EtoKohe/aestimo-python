#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Input File Description:  Quantum well doped AlGaAs/GaAs heterostructure.
# ------------------------------------------------------------------------
# ----------------
# GENERAL SETTINGS
# ----------------

# TEMPERATURE
T = 300.0 #Kelvin

# COMPUTATIONAL SCHEME
# 0: Schrodinger
# 1: Schrodinger + nonparabolicity
# 2: Schrodinger-Poisson
# 3: Schrodinger-Poisson with nonparabolicity
# 4: Schrodinger-Exchange interaction
# 5: Schrodinger-Poisson + Exchange interaction
# 6: Schrodinger-Poisson + Exchange interaction with nonparabolicity
computation_scheme = 8

# Non-parabolic effective mass function
# 0: no energy dependence
# 1: Nelson's effective 2-band model
# 2: k.p model from Vurgaftman's 2001 paper
#meff_method = 2

# Non-parabolic Dispersion Calculations for Fermi-Dirac
#fermi_np_scheme = True*/

# QUANTUM
# Total subband number to be calculated for electrons
subnumber_e = 2
subnumber_h = 2
# APPLIED ELECTRIC FIELD
Fapplied = 0.7#/50e-9 # (V/m)
vmax= 1.4
vmin= 0.0
Each_Step=0.05

# --------------------------------
# REGIONAL SETTINGS FOR SIMULATION
# --------------------------------

# GRID
# For 1D, z-axis is choosen
gridfactor = 1 #nm
maxgridpoints = 200000 #for controlling the size
mat_type='Zincblende'
# REGIONS
# Region input is a two-dimensional list input.
# An example:
# Si p-n diode. Firstly lets picturize the regional input.
#         | Thickness (nm)  | Material | Alloy fraction | Doping(cm^-3) | n or p type |
# Layer 0 |       250.0     |   Si     |      0         |     1e16      |     n       |
# Layer 1 |       250.0     |   Si     |      0         |     1e16      |     p       |
#
# To input this list in Gallium, we use lists as:

material =[                                                 # dont know difference of 'GaAs',0,... and 'GaAs', 0.2...
            [2.5, 'MgO', 0.0, 0.0, 'n','w'],
            [50.0, 'GaAs', 0.0, 1e16, 'n','b'], 
            [30.0, 'GaAs', 0.0, 0.0, 'i','w'],
            [9.0, 'InGaAs', 0.3, 0.0, 'i','b'],
            [30.0, 'GaAs', 0.0, 0.0, 'i','w'],
            #[9.0, 'InGaAs', 0.3, 0.0, 'n','b'],
            #[30.0, 'GaAs', 0.0, 0.0, 'n','w'],
            #[9.0, 'InGaAs', 0.3, 0.0, 'n','b']
            [50.0, 'GaAs', 0.0, 1e16, 'p','w']
            #[300.0, 'GaAs', 0.0, 0.0,  5e18, 'n','w']
            ]


 #----------------------------------------
import numpy as np
x_max = sum([layer[0] for layer in material])
def round2int(x):
    return int(x+0.5)
n_max=round2int(x_max/gridfactor)
#----------------------------------------
dop_profile=np.zeros(n_max)  
#----------------------------------------
Quantum_Regions=False
Quantum_Regions_boundary=np.zeros((2,2))
#----------------------------------------
surface=np.zeros(2)
#surface[0]=-0.6
#---------------------------------------- 
if __name__ == "__main__": #this code allows you to run the input file directly
    input_obj = vars()
    import aestimo_eh
    aestimo_eh.run_aestimo(input_obj)
