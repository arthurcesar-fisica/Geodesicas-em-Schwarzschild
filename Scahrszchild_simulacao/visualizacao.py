from vpython import *
import config as cfg
import random as random
def configurar_cena():
    scene.background = color.black
    scene.width = 800
    scene.height = 600
    scene.center = vector (0, 0, 0)
    buraco_negro = sphere(pos=vec(0,0,0), radius = cfg.r_s, color = color.black)
    for i in range(200):
        x = random.uniform(-500,500)
        y = random.uniform(-500,500)
        z = random.uniform(-500,500)
        sphere (pos = vector(x, y, z), radius = 1, color = color.white)


if __name__ == "__main__":
    configurar_cena()
    
    # Adicione o loop aqui para manter a janela aberta durante o teste
    while True:
        rate(10) # 10 frames por segundo é suficiente para uma cena parada




