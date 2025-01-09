# Catalina Savage
# AST 5263 - Advanced Observational Astronomy
# Homework 4


import numpy as np
import matplotlib.pyplot as plt

import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun  #, FK5
from astropy.time import Time, TimeGPS



# Question 1

# RA in J2000
ra_A = 14*u.hour + 39*u.minute + 36.5*u.second
ra_B = 14*u.hour + 39*u.minute + 35.1*u.second

# declinations
dec_A = -60*u.degree + 50*u.arcminute + 2*u.arcsecond
dec_B = -60*u.degree + 50*u.arcminute + 15*u.arcsecond

# proper motions, RA
pm_raA = -3.679*( u.arcsecond / u.year )
pm_raB = -3.614*( u.arcsecond / u.year )

# proper motions, declination
pm_decA = 0.474*( u.arcsecond / u.year )
pm_decB = 0.803*( u.arcsecond / u.year )

# epochs to use in calculations
epoch = Time( np.linspace(2000,2050,100), format='decimalyear' )

# calculate apparent motions in difference epochs
coord_A = SkyCoord( ra=ra_A,
                    dec=dec_A,
                    pm_ra_cosdec=pm_raA,
                    pm_dec=pm_decA,
                    obstime=epoch )

coord_B = SkyCoord( ra=ra_B,
                    dec=dec_B,
                    pm_ra_cosdec=pm_raB,
                    pm_dec=pm_decB,
                    obstime=epoch )

sep = coord_A.separation( coord_B )
sep_argmin = np.argmin( sep )

sep_epoch = epoch[ sep_argmin ]
sep_min = sep.min()

sep_arcsec = sep_min.to( u.arcsecond )

print( 'Epoch of minimal separation: ', sep_epoch )
print( 'Minimum separation in arcseconds:', sep_arcsec )



# Question 2

# t = np.arange( 1582,10000.1 )
t = np.linspace( 1582,10000 )

t_1 = t - 1580
t_2 = t - 1600
t_3 = t - 1582

t_leap = t_1//4 - t_2//100 + t_2//400

days_cnt  = t_3*365 + t_leap
days_trop = t_3*365.24219

# offset
tau = days_cnt - days_trop
print( tau )

# ( a )
# plot offset as a function of year (??)
plt.figure( figsize=(8,6) )
plt.plot( t, tau )

plt.title( 'Offset Between the Calendar and Tropical Years' )

plt.xlabel( 'Year' )
plt.ylabel( 'Offset, days' )

plt.show()



# Question 3

az = [ 53, 233 ]

alt_min = 20*u.degree  # altitude of sun in sky

lat_psb = 28.6*u.degree
long_ecl = 0*u.degree
long_rate = 360*u.degree / 365.25

# psb = EarthLocation( lat=lat_psb, lon=-(180-az[0]), height=0 )
psb = EarthLocation( lat=lat_psb, lon=-(180-az[long_ecl]), height=0 )

# array containing number of days in a year
one_yr = np.linspace( 1, 365 )

long_sun = long_rate*( one_yr - 80 )  # assign March 20 as Day 0

psb_time = Time( '2018-02-16 12:00:00', scale='utc' ) + one_yr - 1
psb_altaz = AltAz( obstime=psb_time, location=psb )

sun_time = get_sun( psb_time )
sun_altaz = sun_time.transform_to( psb_altaz )

sun_light = sun_altaz.alt.deg > alt_min
sun_day = one_yr[ sun_light ] # not like the weekday

print( "Days of direct sunlight on NW side of PSB's first floor:", sun_day )
