import pygame
import os
from pygame.locals import *
from main.StateManager import getManager
from state.HelpState import HelpState
from state.SettingsState import SettingsState
from state.GameState import GameState
from utility.Image import Image
from utility.Button import Button
from utility.Constants import mainButtonDim, windowDim, loadImage

class MenuState(GameState):
    
    pressed = False
    
    def __init__(self):
        centerx = windowDim / 2
        
        self.images = pygame.sprite.RenderPlain()
        
        #Title
        titleImage, titleRect = loadImage("Title.png")
        titleRect.center = (centerx, 100)
        title = Image(titleImage, titleRect)
        
        #BG
        bgImage, bgRect = loadImage("BG.png")
        bg = Image(bgImage, bgRect)
        
        self.images.add(bg, title)
        
        #Initialize Buttons
        self.buttons = pygame.sprite.RenderPlain()
        self.startButton = Button(centerx, 250, mainButtonDim, "PlayButton.png")
        self.helpButton = Button(centerx, 400, mainButtonDim, "HelpButton.png")
        self.quitButton = Button(centerx, 550, mainButtonDim, "QuitButton.png")
       
        self.buttons.add(self.startButton, self.helpButton, self.quitButton)
        
    def update(self):
        for event in pygame.event.get(): 
            if event.type == QUIT:
                return False
        
        #Buttons is currently pressed
        currPressed = pygame.mouse.get_pressed()[0]    
        
        #Button was released
        released = self.pressed and not currPressed
                
        for button in self.buttons:
            button.update(currPressed)
        
                
        #Behavior of button when clicked
        if released:
            manager = getManager()
            if self.startButton.mouseIn():
                manager.push(SettingsState())
            elif self.helpButton.mouseIn():
                manager.push(HelpState())
            elif self.quitButton.mouseIn():
                return False
                
        self.pressed = currPressed
        return True
            
    def render(self, screen):
        self.images.draw(screen)
        self.buttons.draw(screen)
