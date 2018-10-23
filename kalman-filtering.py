# Downloaded from course lecture slides

# Kalman filter example demo in Python

# A Python implementation of the example given in pages 11-15 of "An
# Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
# University of North Carolina at Chapel Hill, Department of Computer
# Science, TR 95-041,
# http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html

# by Andrew D. Straw

import numpy as np
import pylab as plb

# intial parameters
n_iter = 100
sz = (n_iter,) # size of array
x = -0.37727 # truth value (typo in example at top of p. 13 calls this z)
z = np.random.normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)

Q = 1e-5 # process variance

# allocate space for arrays
xhat=np.zeros(sz)      # a posteri estimate of x
P=np.zeros(sz)         # a posteri error estimate
xhatminus=np.zeros(sz) # a priori estimate of x
Pminus=np.zeros(sz)    # a priori error estimate
K=np.zeros(sz)         # gain or blending factor

R = 1**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = 0.0
P[0] = 1.0

for k in range(1,n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q

    # measurement update
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]

plb.figure()
plb.plot(z,'k+',label='noisy measurements')
plb.plot(xhat,'b-',label='a posteri estimate')
plb.axhline(x,color='g',label='truth value')
plb.legend()
plb.xlabel('Iteration')
plb.ylabel('Voltage')

plb.figure()
valid_iter = range(1,n_iter) # Pminus not valid at step 0
plb.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
plb.xlabel('Iteration')
plb.ylabel('$(Voltage)^2$')
#plb.setp(plb.gca(),'ylim',[0,.01])
plb.show()
