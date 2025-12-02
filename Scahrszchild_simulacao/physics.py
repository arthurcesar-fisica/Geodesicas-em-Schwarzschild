# Bibliotecas
import numpy as np
import config as cfg

# Vamos trabalhar com a Hamiltoniana do sistema 

def hamiltoniana_sistema (t, h):
  x, y, z, px, py, pz = h
  r = np.sqrt(x**2 + y**2 +z**2)
  p_escalar = np.dot(h[:3],h[3:]) # quanto do momento esta na direção radial 
  fator = (1-2*cfg.M*1/r)
  correcao = ((2*cfg.M*(p_escalar))/((r**3)*fator))
  p = h[3:]
  x = h[:3]
  velocidade = p + correcao *x
  aceleracao = -(cfg.M*x*1/(r**3)*((3/fator)*((p_escalar/r)**2)))
  movimento = np.concatenate((velocidade, aceleracao))
  return movimento

def rk4 (t, h, dt):
  k1 = hamiltoniana_sistema(t, h)
  k2 = hamiltoniana_sistema(t+dt/2, h + k1*dt/2)
  k3 = hamiltoniana_sistema(t+dt/2, h +k2*dt/2)
  k4 = hamiltoniana_sistema(t+dt, h+k3*dt)
  novo_h = h+ (dt/6)*(k1 + 2*k2 +2*k3 + k4)
  return novo_h
