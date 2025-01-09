# Catalina Savage
# AST 5263 - Advanced Observational Astronomy
# Homework 3


import numpy             as np
import matplotlib.pyplot as plt


# Point P, degrees
P_lat = 45
P_lon = 50

# range of 1 arcsec to 10 degrees
del_theta = np.linspace( (1/3600), 10, 1000 )

# Point Q, in degrees
Q_lat = 45 + del_theta # 45 degrees and 30 arcsec
Q_lon = 50 + del_theta # 50 degrees and 30 arcsec


# difference between points
diff_lat = Q_lat - P_lat
diff_lon = Q_lon - P_lon

# difference between points in radians
rad_lat = np.radians( Q_lat - P_lat )
rad_lon = np.radians( Q_lon - P_lon )


# formulas
a_dist = np.sin( rad_lat/2 )**2 + np.cos( np.radians(P_lat) ) * np.cos( np.radians(Q_lat) ) * np.sin( rad_lon/2 )**2
s_sph  = np.degrees( 2*np.arctan2( np.sqrt(a_dist), np.sqrt(1-a_dist) ) )
s_euc  = np.sqrt( diff_lat**2 + (diff_lon*np.cos(np.radians(P_lat)))**2 )

# a_dist = np.sin( diff_lat/2 )**2 + np.cos( np.radians(P_lat) ) * np.cos( np.radians(Q_lat) ) * np.sin( diff_lon/2 )**2
# s_sph  = np.degrees( 2*np.arctan2( np.sqrt(a_dist), np.sqrt(1-a_dist) ) )
# s_euc  = np.sqrt( diff_lat**2 + ( diff_lon*np.cos(np.radians(P_lat) ))**2 )



# difference between angular distance calculations
del_s = s_euc - s_sph
print( del_s )


# PLOTS

# linear**2 plot
plt.figure( figsize=(8,6) )
plt.plot( del_theta, del_s )
plt.title( 'Linear Plot of s as a Function of θ' )
plt.xlabel( '∆θ' )
plt.ylabel( '∆s, Difference between triangular approximations' )
plt.show()

# linear*log plot
plt.figure( figsize=(8,6) )
plt.plot( del_theta, del_s )
plt.title( 'Linear-log Plot of s as a Function of θ' )
plt.xlabel( '∆θ' )
plt.ylabel( '∆s' )
# plt.xscale( 'log' )
plt.yscale( 'log' )
plt.show()

# log*log plot
plt.figure( figsize=(8,6) )
plt.plot( del_theta, del_s )
plt.title( 'Log-log Plot of s as a Function of θ' )
plt.xlabel( '∆θ' )
plt.ylabel( '∆s' )
plt.xscale( 'log' )
plt.yscale( 'log' )
plt.show()




acc = np.array( [ 0.1/3600, 1/3600, 0.1/60, 1/60 ] )

acc_s = del_s[ :,np.newaxis ]

acc_idx = np.argmax( acc_s > acc, axis=0 )

del_max = del_theta[ acc_idx ]

# print( del_max )
