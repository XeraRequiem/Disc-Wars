import os
import pygame
from pygame.locals import *
from utility.Line import Line
from entity.Magnet import Magnet

pygame.mixer.init()

playerColors = [(0, 255, 255), (255, 6, 0), (28, 175, 0), (255, 255, 39)]
playerRadius = 15
windowDim = 720
playHeight = 650
playerPos = [(playerRadius + 1, playerRadius + 1),
            (windowDim - (playerRadius + 1), playHeight - (playerRadius + 1)),
            (playerRadius + 1, playHeight - (playerRadius + 1)),
            (windowDim - (playerRadius +1), playerRadius + 1)]

mainButtonDim = (162, 43)
settingsButtonDim = (294, 43)
    
def loadImage(name):
    fullname = os.path.join("..", "assets", "img", name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print (('Cannot load image:', fullname))
        raise SystemExit(message)
    
    return image, image.get_rect()


def loadImageSheet(name, dim):
    image, rect = loadImage(name)
    images = []
    width, height = dim

    for x in range(0, image.get_width(), width):
        rect = pygame.Rect(x, 0, width, height)
        newImage = image.subsurface(rect) 
        images.append(newImage)
        
    return images, images[0].get_rect()

def loadWalls(name):
    file = open(os.path.join("..", "assets", "maps", name), 'r')
    mapWalls = file.read().splitlines()
    
    
    walls = []
    
    for wall in mapWalls:
        coord = wall.split(', ')        
        line = Line(int(coord[0]), int(coord[1]), int(coord[2]), int(coord[3]))
        walls.append(line)
        
    return walls

def loadMagnets(name):
    mapfile = open(os.path.join("..", "assets", "maps", name), 'r')
    mapMagnets = mapfile.read().splitlines()
    
    magnets = pygame.sprite.RenderPlain()
    
    for mapMagnet in mapMagnets:
        coord = mapMagnet.split(', ')        
        magnet = Magnet(int(coord[0]), int(coord[1]), int(coord[2]), int(coord[3]))
        magnets.add(magnet)
        
    return magnets

def loadSound(name):
    class NoneSound:
        def play(self): pass
        
    if not pygame.mixer or not pygame.mixer.get_init():
        sound = NoneSound()
        print(name)
    else:
        fullname = os.path.join(os.path.join("..", "assets", "sound"), name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error as message:
            print("Cannot load sound:", fullname)
            raise SystemExit(message)

    return sound

bounceSound = loadSound("Bounce.wav")
hitSound = loadSound("Hit.wav")