import matplotlib.pyplot as plt
from partícula import Particula

partícula = Particula(x=0, y=0, vx=10, vy=10, massa=1)
dt = 0.1  # [s]
g = -9.8  # [m/s²]

# Listas para armazenar os dados
tempos = [0]
posicoes_x = [partícula.x]
posicoes_y = [partícula.y]
velocidades_x = [partícula.vx]
velocidades_y = [partícula.vy]

# Simulação
tempo_total = 0
while partícula.y <= 0:  # Continua até a partícula atingir o solo
    # Aplica a força da gravidade (apenas no eixo y)
    partícula.newton(fx=0, fy=partícula.massa * g, dt=dt)
    
    # Atualiza o tempo
    tempo_total += dt
    
    # Armazena os dados
    tempos.append(tempo_total)
    posicoes_x.append(partícula.x)
    posicoes_y.append(partícula.y)
    velocidades_x.append(partícula.vx)
    velocidades_y.append(partícula.vy)

# Plot da trajetória
plt.figure(figsize=(10, 6))
plt.plot(posicoes_x, posicoes_y, 'b-', label='Trajetória')
plt.scatter(posicoes_x[0], posicoes_y[0], color='green', label='Início (t=0)')
plt.scatter(posicoes_x[0], posicoes_y[0], color='red', label='Fim (solo)')
plt.xlabel('Posição x (m)')
plt.ylabel('Posição y (m)')
plt.title('Trajetória da Partícula sob Gravidade')
plt.grid(True)
plt.legend()
plt.axis('equal')  # Mantém a proporção dos eixos
plt.show()