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
