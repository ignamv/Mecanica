#!/usr/bin/env python
#--encoding: utf-8 --
import pygame
from math import *

# Scattering por un pozo rectangular de potencial esféricamente simétrico
# V(r) =    0   si r > a
#           -Vo si r < a

# Masa de partículas
m = 1.0
# Energía con que vienen
E = 1.0
# Radio del pozo
a = 1.0
# Potencial
Vo = E/2.0

(ancho,alto) = (800,600)
# Pixeles por metro
escala = 160
def pantalla(x,y):
    return (int(ancho/2+escala*x),int(alto/2-escala*y))
def coordenadas(pos):
    (x,y) = pos
    return ((x-ancho/2.0)/escala,(alto/2.0-y)/escala)
color_circulo = (255,0,0)
color_camino = (255,255,255)

pygame.init()
ventana = pygame.display.set_mode((800,600))
def particula(s):
    # Calculo la intersección con el círculo
    x_choque = -sqrt(a**2-s**2)
    pygame.draw.line(ventana,color_camino,pantalla(-10,s),pantalla(x_choque,s))
    # Nueva velocidad
    v_inf = sqrt(E*2/m)
    v2 = v_inf * sqrt(1+Vo/E)
    alfa = asin(s/a)
    beta = asin(s/a/sqrt(1+Vo/E))
    angulo = 2*beta-alfa
    pygame.draw.line(ventana,color_camino,pantalla(x_choque,s),
                     pantalla(a*cos(angulo),a*sin(angulo)))
    # Velocidad final
    angulof = 2*beta-2*alfa
    pygame.draw.line(ventana,color_camino,pantalla(a*cos(angulo),a*sin(angulo)),
                    pantalla(10*cos(angulof),10*sin(angulof)))
    return

particula(a/2)

pygame.display.flip()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            from os import sys
            sys.exit(0) 
        elif event.type == pygame.MOUSEMOTION:
            ventana.fill((0,0,0))
            # El círculo del potencial
            pygame.draw.circle(ventana,color_circulo,pantalla(0,0),
                               int(escala*a),2)
            # Partícula que entra
            s = coordenadas(pygame.mouse.get_pos())[1]
            if s<a:
                particula(s)
            pygame.display.flip()
        else: 
            pass
            #print event 

