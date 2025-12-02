import numpy as np
from vpython import *
import config as cfg
import physics as phy
import visualizacao as vis

vis.configurar_cena()
h = np.array ([-20*cfg.M, 5.19, 0, 1.0 , 0, 0])
foton = sphere(pos = vector(h[0], h[1], h[2]),make_trail=True, radius = 0.1, color = color.yellow)

#animação do fóton
dt = 0.0005
passo_por_frame = 1000
capturado = False
while True:
    rate(100)
    if not capturado:
        for i in range(passo_por_frame):
            h = phy.rk4(0, h, dt)
            distancia = np.linalg.norm(h[:3])
            if distancia < cfg.r_s: #dentro do horizonte 
                #foton cai na singularidade
                capturado = True
        foton.pos = vector(h[0], h[1], h[2])
    



