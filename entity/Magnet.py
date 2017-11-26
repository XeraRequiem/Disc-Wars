import pygame
from utility.Circle import Circle
from math import cos, sin, atan2, fabs

class Magnet(pygame.sprite.Sprite):
    
    def __init__(self, r, x, y, q):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.r = r        
        self.collCircle = Circle(r, x, y) 
        self.q = q
        self.k = 25
        
        surf = pygame.Surface((2 * r, 2 * r))
        color = (255, 255, 255)
        if q < 0:
            color = (200, 20, 45)
                
        pygame.draw.circle(surf, color, (r, r), r)
        
        self.image = surf
        self.rect = surf.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        
    def forceVector(self, c, p):
        dx = self.x - c.x
        dy = self.y - c.y
        angle = atan2(dy, dx)
            
        r = fabs(dx * dx + dy * dy)
        
        f = self.k * (self.q * p / r) 
        return f * cos(angle), f * sin(angle)