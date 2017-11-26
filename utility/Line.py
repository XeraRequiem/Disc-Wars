import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        dx = x2 - x1
        dy = y2 - y1
        self.length = math.sqrt(dx * dx + dy * dy)
        self.angle = math.atan2(dy, dx)
        
    def getLength(self):
        return self.length
    
    def getAngle(self):
        return self.angle