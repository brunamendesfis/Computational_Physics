import matplotlib.pyplot as plt
from partícula import Particula

partícula = Particula(x=0, y=0, vx=10, vy=10, massa=1)
dt = 0.1  # [s]
g = -9.8  # [m/s²]

tempos, posicoes_x, posicoes_y, velocidades_x, velocidades_y = partícula.evoluicao_temporal(dt=dt, g=g)

plt.figure(figsize=(10, 6))
plt.plot(posicoes_x, posicoes_y, 'b-', label='Trajectory')
plt.scatter(posicoes_x[0], posicoes_y[0], color='green', label='Start (t=0)')
plt.scatter(posicoes_x[-1], posicoes_y[-1], color='red', label='End')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Particle Trajectory under Gravity')
plt.grid(True)
plt.legend()
plt.ylim(-0.5, 6)
plt.show()