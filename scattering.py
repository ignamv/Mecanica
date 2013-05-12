#!/usr/bin/env python2
#--encoding: utf-8 --
"""
scattering
==========
Show the trajectory of a classical particle scattered by a spherically
symmetric central potential

V(r) =  / 0          if r > radius
        \ -potential if r < radius

"""

import pygame
from math import asin, sqrt, cos, sin

# Particle mass [kg]
mass = 1.0
# Energy [J]
energy = 1.0
# Potential well radius [m]
radius = 1.0
# Potential value [J]
potential = energy/2.0

width, height = 800, 600
# Pixels per metre
scale = 160 
circle_color = (255, 0, 0)
trajectory_color = (255, 255, 255)

# Functions to convert between coordinate systems
def to_screen(x, y):
    return (int(width/2+scale*x), int(height/2-scale*y))
def from_screen(pos):
    (x, y) = pos
    return ((x-width/2.0)/scale, (height/2.0-y)/scale)

pygame.init()
window = pygame.display.set_mode((800, 600))
def draw_trajectory(impact_parameter):
    # Calculate intersection with potential well
    x_intersection = -sqrt(radius**2-impact_parameter**2)
    pygame.draw.line(window, trajectory_color, 
                     to_screen(-10, impact_parameter),
                     to_screen(x_intersection, impact_parameter))
    # Velocity inside the well
    v_inf = sqrt(energy*2/mass)
    # Varius angles
    alfa = asin(s/radius)
    beta = asin(s/radius/sqrt(1+potential/energy))
    angle = 2*beta-alfa
    pygame.draw.line(window, trajectory_color,
                     to_screen(x_intersection, impact_parameter),
                     to_screen(radius*cos(angle), radius*sin(angle)))
    # Final angle
    anglef = 2*beta-2*alfa
    pygame.draw.line(window, trajectory_color,
                     to_screen(radius*cos(angle), radius*sin(angle)),
                     to_screen(10*cos(anglef), 10*sin(anglef)))
    return

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            from os import sys
            sys.exit(0) 
        elif event.type == pygame.MOUSEMOTION:
            window.fill((0, 0, 0))
            # Draw potential well boundary
            pygame.draw.circle(window, circle_color, to_screen(0, 0),
                               int(scale*radius), 2)
            s = from_screen(pygame.mouse.get_pos())[1]
            if abs(s)<radius:
                draw_trajectory(s)
            pygame.display.flip()
