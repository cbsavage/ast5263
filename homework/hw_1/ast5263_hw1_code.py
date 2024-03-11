# Catalina Savage
# AST 5263 - Advanced Observational Astronomy
# Homework 1


# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
from scipy import *



# Problem 1


# PART A

# constants
k   = 1.38e-23  # Stefan-Boltzmann constant, J/K
h   = 6.626e-34 # Planck's constant, J/Hz
c   = 3e+8      # m/s
T_a = 2000      # Kelvin
C_a = 1         # (in proper units) THIS IS AN ASSUMPTION


# values
wv_a = [ 0.37, 0.44, 0.55, 0.70, 1.20, 1.60, 2.20, 3.60 ]                # star A's wavelength, microns
mg_a = [ 9.432, 7.196, 4.839, 2.832, -0.148, -1.126, -1.871, -2.410 ]    # star A's magnitude

wv_b = [ 5.00, 8.90, 9.70, 10.60, 11.70, 12.50, 18.70, 20.60 ]           # star B's wavelength, microns
mg_b = [ -2.107, -0.966, -0.822, -0.685, -0.548, -0.464, -0.069, 0.002 ] # star B's magnitude


# convert wavelength to frequency
freq_a = [ c/wv for wv in wv_a ]

freq_b = [ c/wv for wv in wv_b ]


# ratio = 10**( -0.4*mg )
ratio_a = [ 10**( -0.4*mg ) for mg in mg_a ]

ratio_b = [ 10**( -0.4*mg ) for mg in mg_b ]


# Bfreq_a = ( 2*h*(freq_a**3) / c**2 ) * ( 1 / np.exp( h*freq_a/k*T_a )-1 )               Why doesn't this work...
Bfreq_a = [ (( 2*h*(freq**3) / c**2 ) * ( 1 / np.exp( h*freq/k*T_a )-1 )) for freq in freq_a ] # ...but this does?

# Fb_a = B_v / Fa_ratio
F_a = [ B_freq * C_a for B_freq in Bfreq_a ]
# Fb_b = B_v / Fb_ratio
F_b = []

len_wvb = len( wv_b )
print( 'Amount of wavelengths for Star B:', len_wvb )

for i in range( len_wvb ):
    idx_a = wv_a.index( min(wv_a, key=lambda x:abs( x - wv_b[i])) )
    F_b.append( F_a[idx_a] / ratio_b[i] )
    print( wv_b[i], F_b[i] )


# PART B, LOG-LOG PLOT
# plot flux vs wavelength

plt.figure( figsize=(8,6) )
plt.plot( wv_b, F_b, marker='o' )

plt.xlabel( 'Wavelength (micron)', fontsize=12 )
plt.ylabel( 'Flux Density (W/m**2)', fontsize=12 )

plt.title( "Wavelength vs. Star B's Flux Density", fontsize=16 )

plt.show()



# Problem 2

# read in data files
# sol_spec = pd.read_table( 'SolarSpectrum.txt', delimiter='\t' )
# jc_filt  = pd.read_table( 'Johnson-Cousin_Filters.txt', delimiter='\t' )












# Problem 3
# 3a: plot solid angle as a function of lunar phase's phase angle, alpha

# might have to convert smth??
#  Date__(UT)__HR:MN       APmag   S-brt       phi  PAB-LON  PAB-LAT

# alpha = phi column, already in degrees

# plt.figure( figsize=(8,6) )
# # plt.plot( phase_angle, solid angle )

# plt.xlabel()
# plt.ylabel()

# plt.show()