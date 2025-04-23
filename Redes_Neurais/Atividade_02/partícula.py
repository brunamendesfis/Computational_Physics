class Particula():

    def __init__(self, x, y, vx, vy, massa):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.massa = massa

    def newton(self, fx, fy, dt):
        """ Função para aplicar a Segunda Lei de Newton e atualizar a velocidade e a posição da partícula.

        Parâmetros:
        
        fx (float): Calcula a força na direção x (N)
        fy (float): Calcula a força na direção y (N)
        dt (float): Intervalo de tempo (s)

        """
        
        # Cálculo das acelarações me cada eixo:
        ax = fx/self.massa
        ay = fy/self.massa
        
        # Atualiza as velocidades:
        self.vx += ax*dt
        self.vy += ay*dt

        # Atualiza as posições:
        self.x = self.vx*dt
        self.y = self.vy*dt

        fx = self.massa * self.vx/dt
        fy = self.massa * self.vy/dt
