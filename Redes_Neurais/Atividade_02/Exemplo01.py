import matplotlib.pyplot as plt
from partícula import Particula

partícula = Particula(x=0, y=0, vx=10, vy=10, massa=1)
dt = 0.1  # [s]
g = -9.8  # [m/s²]

# Lists to store the data
tempos = [0]
posicoes_x = [partícula.x]
posicoes_y = [partícula.y]
velocidades_x = [partícula.vx]
velocidades_y = [partícula.vy]

# Simulation loop
tempo_total = 0
while partícula.y >= 0:
    partícula.newton(fx=0, fy=partícula.massa * g, dt=dt)
    tempo_total += dt
    tempos.append(tempo_total)
    posicoes_x.append(partícula.x)
    posicoes_y.append(partícula.y)
    velocidades_x.append(partícula.vx)
    velocidades_y.append(partícula.vy)

if posicoes_y[-1] < 0:
    posicoes_x.pop()
    posicoes_y.pop()
    tempos.pop()
    velocidades_x.pop()
    velocidades_y.pop()

# Linear interpolation to find x when y=0
if posicoes_y[-1] > 0 and velocidades_y[-1] < 0:
    y1 = posicoes_y[-2]
    y2 = posicoes_y[-1]
    x1 = posicoes_x[-2]
    x2 = posicoes_x[-1]
    t1 = tempos[-2]
    t2 = tempos[-1]

    frac = y1 / (y1 - y2)
    x_solo = x1 + frac * (x2 - x1)
    t_solo = t1 + frac * (t2 - t1)
    posicoes_x.append(x_solo)
    posicoes_y.append(0)
    tempos.append(t_solo)

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