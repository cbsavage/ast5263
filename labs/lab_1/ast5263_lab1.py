# Catalina Savage
# AST 5263
# Lab 1 - Radio Telescope

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from astropy import *
from scipy   import *


# Problem 1

# constants
freq = 1420.40575177 # MHz
d    = 1.0           # m
wvl  = 0.2111        # m = 21.11 cm

# formulas
theta_rad = 1.22 * ( wvl/d )          # Rayleigh criterion, radians
theta_deg = theta_rad * ( 180/np.pi ) # convert radians to degrees

print( "Problem 1:" )
print( f"The Rayleigh criterion for Robinson Observatory's radio telescope is {theta_deg} degrees." )


# Problem 2

# constants
sol_h = 23  # solar hours
sol_m = 56  # solar minutes
sol_s = 3.1 # solar seconds

exp_t = 2   # exposure time, minutes

# convert solar time from hr/min/sec to minutes
sol_hm = sol_h * 60
sol_sm = sol_s * ( 1/60 )

sol_mtot = sol_hm + sol_m + sol_sm  # total minutes in a solar day
exp_a    = ( exp_t*360 ) / sol_mtot # convert minutes to degrees

print( "Problem 2:" )
print( f'In a 2-minute exposure we used to collect data, the sky spins through {exp_a} degrees.' )


# Problem 3

