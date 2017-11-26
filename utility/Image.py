import pygame

class Image(pygame.sprite.Sprite):
    
    def __init__(self, image, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = rect
            