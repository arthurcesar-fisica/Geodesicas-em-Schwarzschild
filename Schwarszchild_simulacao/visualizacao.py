from vpython import *
import config as cfg
import random as random
import numpy as np

def configurar_cena():
    scene.background = color.black
    scene.width = 1400
    scene.height = 800
    scene.center = vector (0, 0, 0)
    buraco_negro = sphere(pos=vec(0,0,0), radius = cfg.r_s, color = color.black)
    for i in range(350):
        x = random.uniform(-500,500)
        y = random.uniform(-500,500)
        z = random.uniform(-500,500)
        sphere (pos = vector(x, y, z), radius = 0.6, color = color.white)


def criar_grade(tamanho=40, espacamento=5):
    
    z_fundo = -20
    cor_grade = vector(0.5, 0.5, 0.5)

    for x in np.arange(-tamanho, tamanho + espacamento, espacamento):
        cylinder(
            pos=vector(x, -tamanho, z_fundo),
            axis=vector(0, 2*tamanho, 0),
            radius=0.05,
            color=cor_grade
        )

    for y in np.arange(-tamanho, tamanho + espacamento, espacamento):
        cylinder(
            pos=vector(-tamanho, y, z_fundo),
            axis=vector(2*tamanho, 0, 0),
            radius=0.05,
            color=cor_grade
        )
if __name__ == "__main__":
    configurar_cena()
    
    # Adicione o loop aqui para manter a janela aberta durante o teste
    while True:
        rate(10) # 10 frames por segundo é suficiente para uma cena parada




