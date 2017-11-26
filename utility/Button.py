import pygame
from utility.Constants import loadImageSheet

class Button(pygame.sprite.Sprite):
    
    def __init__(self, centerx, centery, dim, name):
        pygame.sprite.Sprite.__init__(self)
        self.images, self. rect = loadImageSheet(name, dim)
        self.image = self.images[0]
        self.rect.center = (centerx, centery)
        
    def mouseIn(self):
        mx, my = pygame.mouse.get_pos()
        #Mouse is within bounds of box
        return mx > self.rect.left and mx < self.rect.right and my > self.rect.top and my < self.rect.bottom
        
    def setState(self, state):
        self.image = self.images[state]
        
    def update(self, pressed):
        currMouseIn = self.mouseIn()
        
        if currMouseIn:
            if pressed:
                self.setState(2)
            else:
                self.setState(1)
        else:
            self.setState(0)