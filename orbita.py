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
def elastico(y,t,A):
    # A = k*m/L²
    return sp.array([y[1],-y[0]+A*y[0]**(-3)])
def prob4(y,t,A):
    # A = 2*m*k/L²
    return sp.array([y[1],y[0]*(-1-A)])
def kepler(y,t,A):
    # A = G*M*m²/L² = G*M/r⁴/(dTheta/dT)²
    # Parece raro pero las m se cancelan y queda independiente de m
    return sp.array([y[1],-y[0]+A])

t = sp.linspace(0,2*sp.pi,100)
u = integrate.odeint(prob4,sp.array([1,0]),t,(1,))

x = sp.cos(t)/u[:,0]
y = sp.sin(t)/u[:,0]
pylab.scatter(x,y)
# Marco el origen
pylab.scatter([0],[0],marker='x')
pylab.show()
