#!/usr/bin/env python2
#--encoding: utf-8 --

"""
orbita
======
Plot orbits that result from varius central potentials
"""

# Equation for motion in a central potential: u''+u=-m/L²*dV/du
# Where:
# - u = 1/r
# - u'' = d²u/dTheta²
# - m: Mass
# - L: Angular momentum

import scipy as sp
from scipy import integrate
import pylab

# These functions must return [u',u''] calculated from y=[u,u']
def hooke(y,t,A):
    # A = k*m/L²
    return sp.array([y[1],-y[0]+A*y[0]**(-3)])
def kepler(y,t,A):
    # A = G*M*m²/L² = G*M/r⁴/(dTheta/dT)²
    return sp.array([y[1],-y[0]+A])

t = sp.linspace(0,2*sp.pi,100)
u = integrate.odeint(kepler,sp.array([1,0]),t,(1,))

x = sp.cos(t)/u[:,0]
y = sp.sin(t)/u[:,0]
pylab.plot(x,y)
# Marco el origen
pylab.scatter([0],[0],marker='x')
pylab.show()
