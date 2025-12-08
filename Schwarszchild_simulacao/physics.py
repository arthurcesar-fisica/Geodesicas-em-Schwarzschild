# Bibliotecas
import numpy as np
import config as cfg

# Vamos trabalhar com a Hamiltoniana do sistema 

def hamiltoniana_sistema(t, h):
    x, y, z, px, py, pz = h
    
    # 1. Vetores
    r_vec = np.array([x, y, z])
    v_vec = np.array([px, py, pz])
    
    # 2. Distância ao quadrado e Distância
    r_sq = np.dot(r_vec, r_vec)
    r = np.sqrt(r_sq)
    
    # 3. Momento Angular (L = r x v)
  
    L_vec = np.cross(r_vec, v_vec)
    L_sq = np.dot(L_vec, L_vec) 
    
    # 4. A Força 
    # Para a luz, a força radial efetiva vem do termo -3ML^2/r^4
    # Como queremos aceleração vetorial, multiplicamos por (x/r), ficando r^5 no denominador
    
    # Fator de magnitude da força
    # 3 * M * L^2 / r^5
    fator_forca = 3.0 * cfg.M * L_sq / (r_sq * r_sq * r)
    
    # Aceleração aponta para o centro (-x)
    dpx = -fator_forca * x
    dpy = -fator_forca * y
    dpz = -fator_forca * z
    
    # Velocidade é o próprio momento (para luz c=1)
    return np.array([px, py, pz, dpx, dpy, dpz])
def rk4 (t, h, dt):
  k1 = hamiltoniana_sistema(t, h)
  k2 = hamiltoniana_sistema(t+dt/2, h + k1*dt/2)
  k3 = hamiltoniana_sistema(t+dt/2, h +k2*dt/2)
  k4 = hamiltoniana_sistema(t+dt, h+k3*dt)
  novo_h = h+ (dt/6)*(k1 + 2*k2 +2*k3 + k4)
  return novo_h
