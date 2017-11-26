import pygame
from main.StateManager import getManager
from state.MenuState import MenuState
from utility.Constants import windowDim
from pygame.locals import *

class Main:
	manager = getManager()
	playing = True
		
	#Initialize variables necessary for game & start start loop
	def start(self):
		#Initializations
		pygame.init()
		pygame.display.set_caption('Disc Wars')
		pygame.mouse.set_visible(1)
		clock = pygame.time.Clock()
	
		#Initial State
		self.manager.push(MenuState())
		
		#Screen
		self.screen = pygame.display.set_mode((windowDim, windowDim))
		
		#Background
		self.background = pygame.Surface(self.screen.get_size())
		self.background.fill((0, 0, 0))
	
		#Gameloop
		while self.playing:
			clock.tick(60)
			self.update()
			self.render(self.screen)
		
	def update(self):
		self.playing = self.manager.update()
	
	def render(self, screen):
		screen.blit(self.background, (0, 0))
		self.manager.render(screen)
		pygame.display.flip()
		
mainGame = Main()

def getMain():
	return mainGame
	
if __name__ == "__main__":
	try:
		mainGame.start()
	finally:
		pygame.quit()