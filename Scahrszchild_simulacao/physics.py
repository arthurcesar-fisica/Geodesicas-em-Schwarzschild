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
