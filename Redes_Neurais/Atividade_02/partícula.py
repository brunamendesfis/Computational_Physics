class partícula():

    def __init__(self, x, y, vx, vy, massa):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.massa = massa

    def newton(self, fx, fy, dt):
        fx = self.massa * self.vx/dt
        fy = self.massa * self.vy/dt
        return fx, fy
    
x = 0
y = 0
vx = 10 # m/s
vy = 10 # m/s
m = 1 # kg

