import pygame
from main.StateManager import getManager
from state.GameState import GameState
from state.PlayState import PlayState
from utility.Button import Button
from pygame.locals import *
from utility.Image import Image
from utility.Constants import settingsButtonDim, windowDim, loadImage

class SettingsState(GameState):
    
    pressed = False
    
    def __init__(self):
        self.players = -1
        centerx = windowDim / 2 
        
        #BG
        self.images = pygame.sprite.RenderPlain()
        bgImage, bgRect = loadImage("BG.png")
        bg = Image(bgImage, bgRect)
        self.images.add(bg)

        #Initialize Buttons
        self.buttons = pygame.sprite.RenderPlain()
        self.twoPlayersButton = Button(centerx, 150, settingsButtonDim, "2PlayerButton.png")
        self.threePlayersButton = Button(centerx, 300, settingsButtonDim, "3PlayerButton.png")
        self.fourPlayersButton = Button(centerx, 450, settingsButtonDim, "4PlayerButton.png")
        
        self.buttons.add(self.twoPlayersButton, self.threePlayersButton, self.fourPlayersButton)
    
    def update(self):
        players = -1
        
        for event in pygame.event.get(): 
            if event.type == QUIT:
                return False
            
        currPressed = pygame.mouse.get_pressed()[0]
    
        for button in self.buttons:
            button.update(currPressed)
            
        released = not currPressed and self.pressed
        
        if released:
            if self.twoPlayersButton.mouseIn():
                players = 2
            if self.threePlayersButton.mouseIn():
                players = 3
            if self.fourPlayersButton.mouseIn():
                players = 4
                
        if players is not -1:
            getManager().set(PlayState(players))
    
        self.pressed = currPressed
        return True
        
    def render(self, screen):
        self.images.draw(screen)
        self.buttons.draw(screen)