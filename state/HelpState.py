from state.GameState import GameState
from utility.Button import Button
from pygame.locals import *
from main.StateManager import getManager
import pygame

class HelpState(GameState):
    
    def __init__(self):
        #Initialize Buttons
        self.returnButton = Button(50, 50, (50, 50), "ReturnButton.png")
        self.buttons = pygame.sprite.RenderPlain()
        self.buttons.add(self.returnButton)
        self.pressed = False        
        
    def update(self):
        for event in pygame.event.get(): 
            if event.type == QUIT:
                return False
        currPressed = pygame.mouse.get_pressed()[0]
        released = self.pressed and not currPressed

        self.returnButton.update(currPressed)

        if self.returnButton.mouseIn() and released:
            getManager().pop()
        
        self.pressed = currPressed
        return True
        
        
    def render(self, screen):
        self.buttons.draw(screen)