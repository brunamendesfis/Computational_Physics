class Particula():

    def __init__(self, x, y, vx, vy, massa):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.massa = massa

    def newton(self, fx, fy, dt):
        """ Function to apply Newton's Second Law and update the velocity and position of the particle.

        Parameters:
        
        fx (float): Force in the x direction (N)
        fy (float): Force in the y direction (N)
        dt (float): Time interval (s)

        """
        
        # The acceleration for each axis
        ax = fx/self.massa
        ay = fy/self.massa
        
        # Update the velocity and position
        self.vx += ax*dt
        self.vy += ay*dt
        self.x += self.vx*dt
        self.y += self.vy*dt

    def evoluicao_temporal(self, dt, g):
        tempos = [0]
        posicoes_x = [self.x]
        posicoes_y = [self.y]
        velocidades_x = [self.vx]
        velocidades_y = [self.vy]
        tempo_total = 0

        while self.y >= 0:
            self.newton(fx=0, fy=self.massa * g, dt=dt)
            tempo_total += dt
            tempos.append(tempo_total)
            posicoes_x.append(self.x)
            posicoes_y.append(self.y)
            velocidades_x.append(self.vx)
            velocidades_y.append(self.vy)

        if posicoes_y[-1] < 0:
            posicoes_x.pop()
            posicoes_y.pop()
            tempos.pop()
            velocidades_x.pop()
            velocidades_y.pop()

        # Interpolação linear para y=0
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

        return tempos, posicoes_x, posicoes_y, velocidades_x, velocidades_y
