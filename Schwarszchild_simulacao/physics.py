# Bibliotecas
import numpy as np
import config as cfg

# Vamos trabalhar com a Hamiltoniana do sistema 

def aceleracao_luz(r_vec, L_sq, M):

    # 1. Magnitudes
    r_sq = np.dot(r_vec, r_vec)
    r = np.sqrt(r_sq)
    
    # 2. Fator de magnitude da força (Eq. das geodésicas nulas)
    # F/m = -3 * M * L^2 / r^5  (apontando para o centro)
    fator = 3.0 * M * L_sq / (r_sq**2 * r)
    
    # 3. Vetor aceleração (aponta contra r_vec)
    a_vec = -fator * r_vec
    
    return a_vec

def aceleracao_materia(r_vec, L_sq, M):

    r_sq = np.dot(r_vec, r_vec)
    r = np.sqrt(r_sq)
    fator = M / (r_sq * r) 
    
    return -fator * r_vec

def velocity_verlet(t, r, v, dt, aceleracao_func):

    
    # 1. Calcula a aceleração atual com a posição antiga
    a_atual = aceleracao_func(t, r)
    
    # 2. Meio passo da velocidade
    v_meio = v + 0.5 * a_atual * dt
    
    # 3. Passo cheio da posição (usando v_meio)
    novo_r = r + v_meio * dt
    
    # 4. Calcula a nova aceleração com a nova posição
    a_nova = aceleracao_func(t + dt, novo_r)
    
    # 5. Completa o passo da velocidade
    novo_v = v_meio + 0.5 * a_nova * dt
    
    return novo_r, novo_v

# Disco de acreção 
def velocidade_orbital_circular(posicao):
   x, y, z = posicao
   
   #distancia radial:
   r = np.sqrt(x**2 + y**2 + z**2)
   
   #para a velocidade (v = sqrt(GM/r) => sqrt(cfg.M/r)) unidades config.
   v_mag = np.sqrt(cfg.M/r)

  #vetor velocidade perpendicular ao raio
   vx = -y / r * v_mag
   vy =  x / r * v_mag
   vz = 0 # Disco plano
   return np.array([vx, vy, vz])

'''def hamiltoniana_sistema(t, h):
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
    return np.array([px, py, pz, dpx, dpy, dpz])'''

'''def rk4 (t, h, dt):
  k1 = hamiltoniana_sistema(t, h)
  k2 = hamiltoniana_sistema(t+dt/2, h + k1*dt/2)
  k3 = hamiltoniana_sistema(t+dt/2, h +k2*dt/2)
  k4 = hamiltoniana_sistema(t+dt, h+k3*dt)
  novo_h = h+ (dt/6)*(k1 + 2*k2 +2*k3 + k4)
  return novo_h'''

