class Circle:

    def __init__(self, rad, x, y):
        self.rad = rad
        self.x = x
        self.y = y
        self.right = x + rad
        self.left = x - rad
        self.top = y - rad
        self.bottom = y + rad
        
    def add(self, vx, vy):
        self.x += vx
        self.y += vy
        
    def getPosition(self):
        return self.x, self.y
    
    def getRadius(self):
        return self.rad
    
    def set(self, x, y):
        self.x = x
        self.y = y