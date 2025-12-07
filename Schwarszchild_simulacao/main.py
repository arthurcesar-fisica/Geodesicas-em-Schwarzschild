import numpy as np
from vpython import *
import config as cfg
import physics as phy
import visualizacao as vis

vis.configurar_cena()
vis.criar_grade()

#gerando fótons 
alturas = [5.0, (3/2) * np.sqrt(3) * cfg.r_s, 5.5, 6.0, 7.0 ]
lista_h = []
lista_esferas = []


# Vamos criar uma grade de 15x5 fótons
'''
alturas_y = np.linspace(4.5, 8.0, 5)
profundidades_z = np.linspace(-2.0, 2.0, 5)

print(f"Iniciando com {len(alturas_y) * len(profundidades_z)} fótons...")

# Loop duplo para criar a parede
for y in alturas_y:
    for z in profundidades_z:
        h = np.array([-20*cfg.M, y, z, 1.0, 0, 0])
        lista_h.append(h)
        
        # Esferas menores e com rastro mais fino para não poluir
        # Usamos uma cor ciano claro para parecer "luz"
        esfera = sphere(pos=vector(h[0], h[1], h[2]), 
                        make_trail=True, trail_radius=0.02, 
                        radius=0.1, color=color.yellow, opacity=0.6)
        lista_esferas.append(esfera)'''

cores =[color.red, color.orange, color.yellow, color.blue, color.cyan]
for i in range(len(alturas)):
    y_inicial = alturas[i]
    h = np.array([-20*cfg.M, y_inicial, 0.0, 1.0, 0.0, 0.0])
    lista_h.append(h)
    esfera = sphere(pos = vec(h[0], h[1], h[2]), make_trail = True, radius = 0.1, color = cores[i])
    lista_esferas.append(esfera)

h = np.array ([-20*cfg.M, 5.25, 0.0, 1.0 , 0.0, 0.0])
foton = sphere(pos = vector(h[0], h[1], h[2]),make_trail=True, radius = 0.1, color = color.yellow)

#animação dos fótons
dt = 0.00005
passo_por_frame = 1000
capturados = [False]*len(lista_h)
while True:
    rate(60)
    for i in range(len(lista_h)):
        #se o foton ainda não caiu
        if not capturados[i]:
            h_temp = lista_h[i]
            for _ in range(passo_por_frame):
                h_temp = phy.rk4(0, h_temp, dt)
                distancia = np.linalg.norm(h_temp[:3])
                if distancia < cfg.r_s:
                    capturados[i] = True
                    h_temp[:3] = h_temp[:3]*(cfg.r_s/distancia)
                    break
            lista_h[i] = h_temp
            lista_esferas[i].pos = vector(h_temp[0], h_temp[1], h_temp[2])


