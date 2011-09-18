#!/usr/bin/env python
#--encoding: utf-8 --

# Ecuación: u''+u=-m/L²*dV/du
# Corresponde a la órbita de una masa en un potencial central
# u = 1/r
# u'' = d²u/dTheta²
# m: Masa
# L: Momento angular

import scipy as sp
from scipy import integrate
import pylab

# y = [u,u']
def cuadratico(y,t,A):
    # A = k*m/L²
    return sp.array([y[1],-y[0]+A*y[0]**(-3)])
def kepler(y,t,A):
    # A = G*M*m²/L² = G*M/r⁴/(dTheta/dT)²
    # Parece raro pero las m se cancelan y queda independiente de m
    return sp.array([y[1],-y[0]+A])

t = sp.linspace(0,2*sp.pi,1000)
y = integrate.odeint(kepler,sp.array([1,0.5]),t,(2,))

x = sp.cos(t)/y[:,0]
y = sp.sin(t)/y[:,0]
pylab.plot(x,y)
pylab.show()
