import numpy as np
from vpython import *
import config as cfg
import physics as phy
import visualizacao as vis

vis.configurar_cena()
h = np.array ([-10*cfg.M, 5, 0, 1.0 , 0, 0])
foton = sphere(pos = vector(h[0], h[1], h[2]),make_trail=True, radius = 0.1, color = color.yellow)

#animação do fóton
dt = 0.000005
passo_por_frame = 1000
while True:
    rate(200)
    for i in range(passo_por_frame):
        derivadas = phy.hamiltoniana_sistema(0, h)
        h = h + derivadas * dt
    foton.pos = vector(h[0], h[1], h[2])
    



