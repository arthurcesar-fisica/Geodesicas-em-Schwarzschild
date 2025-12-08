import numpy as np
from vpython import *
import config as cfg
import physics as phy
import visualizacao as vis

# ---  CENA ---
vis.configurar_cena()
vis.criar_grade()

# --- 1. Fótons ---
alturas = [5.0, (3/2) * np.sqrt(3) * cfg.r_s, 5.5, 6.0, 7.0]
lista_objetos = [] 

cores = [color.red, color.white, color.magenta, color.blue, color.cyan]

for i in range(len(alturas)):
    y_inicial = alturas[i]
    # Posição e Velocidade
    r = np.array([-50*cfg.M, y_inicial, 0.0])
    v = np.array([1.0, 0.0, 0.0]) # Luz vindo da esquerda (vx=1, c=1)
    
    # Visual
    esfera = sphere(pos=vec(r[0], r[1], r[2]), make_trail=True, radius=0.1, color=cores[i])
    
    # Preparação para o Verlet (Cálculos iniciais)
    L_vec = np.cross(r, v)
    L_sq = np.dot(L_vec, L_vec)
    a_atual = phy.aceleracao_luz(r, L_sq, cfg.M)
    
    lista_objetos.append({
        'r': r, 
        'v': v, 
        'a': a_atual, 
        'L_sq': L_sq, 
        'obj': esfera, 
        'ativo': True,
        'tipo': 'foton',
        'func': phy.aceleracao_luz
    })

# --- 2. PREPARAÇÃO DO DISCO DE ACREÇÃO ---
num_particulas = 500
raio_min = 3.5 * cfg.r_s 
raio_max = 8.0 * cfg.r_s  
amarelo_claro = vector(1, 0.8, 0.2)

for i in range(num_particulas):
    # Geometria
    r_mag = np.random.uniform(raio_min, raio_max)
    theta = np.random.uniform(0, 2*np.pi)
    
    x = r_mag * np.cos(theta)
    z = r_mag * np.sin(theta)   
    y = np.random.normal(0, 0.1 * cfg.r_s) 
    
    r_vec = np.array([x, y, z])

    # Velocidade Orbital
    v_mag = np.sqrt(cfg.G * cfg.M / r_mag)
    vx = -v_mag * (z / r_mag)
    vz = v_mag * (x / r_mag)
    vy = 0 
    v_vec = np.array([vx, vy, vz]) 
    
    # Visual
    esfera = sphere(pos=vector(x, y, z), 
                    radius=0.1,
                    color=amarelo_claro, 
                    opacity = 0.3,
                    emissive=True,
                    make_trail=True, trail_radius=0.05, retain=10)
    
    # Preparação Verlet
    L_vec = np.cross(r_vec, v_vec)
    L_sq = np.dot(L_vec, L_vec)
    func_fisica = phy.aceleracao_materia 
    a_atual = func_fisica(r_vec, L_sq, cfg.M)
    
    lista_objetos.append({
        'r': r_vec, 
        'v': v_vec, 
        'a': a_atual, 
        'L_sq': L_sq, 
        'obj': esfera, 
        'ativo': True,
        'tipo': 'disco',
        'func': func_fisica
        
    })

# --- 3. LOOP DE ANIMAÇÃO COM VERLET ---
dt = 0.05 # Passo de tempo 
passo_por_frame = 5 # Quantos cálculos por frame de vídeo

print("Iniciando simulação com Velocity Verlet...")

while True:
    rate(60) # 60 FPS
    
    # Loop de cálculo (física)
    for _ in range(passo_por_frame):
        for p in lista_objetos:
            if not p['ativo']: continue
            
            # --- ALGORITMO VELOCITY VERLET ---
            # 1. Meia velocidade
            v_meio = p['v'] + 0.5 * p['a'] * dt
            
            # 2. Posição inteira
            r_novo = p['r'] + v_meio * dt
            
            # Checagem de colisão (Buraco Negro)
            dist = np.linalg.norm(r_novo)
            if dist < 2 * cfg.M: # Horizonte de eventos (aprox)
                p['ativo'] = False
                p['obj'].visible = False # Some com a partícula
                continue
            
            # 3. Nova aceleração (Física)
            a_nova = p['func'](r_novo, p['L_sq'], cfg.M)
            
            # 4. Fecha velocidade
            v_novo = v_meio + 0.5 * a_nova * dt
            
            # Atualiza estado
            p['r'] = r_novo
            p['v'] = v_novo
            p['a'] = a_nova

    # Loop de desenho (apenas uma vez por frame)
    for p in lista_objetos:
        if p['ativo']:
            p['obj'].pos = vector(p['r'][0], p['r'][1], p['r'][2])
