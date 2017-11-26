import pygame
from pygame.locals import *
from utility.Circle import Circle
from utility.Constants import playerColors, playerPos, playerRadius, windowDim, playHeight
from utility.Collision import *

class Player (pygame.sprite.Sprite):
	
	movement = 250
	speed = 2
	used = 0
	dead = False
	shotTaken = False
	x = y = 0
	
	def __init__(self, index):
		pygame.sprite.Sprite.__init__(self)
			
		surf = pygame.Surface((2 * playerRadius, 2 * playerRadius))
		
		self.index = index
		
		pygame.draw.circle(surf, playerColors[index], (playerRadius, playerRadius), playerRadius)
		self.x, self.y = playerPos[index]
		
		self.image = surf
		self.rect = surf.get_rect()
		self.rect.centerx = self.x
		self.rect.centery = self.y
		
		self.collCircle = Circle(playerRadius, self.rect.centerx, self.rect.centery)

	def render(self, screen):
		width = 200 * (1 - self.used / self.movement)
		
		outerRect = pygame.Rect(0, 700, 210, 50)
		innerRect = pygame.Rect(5, 705, 200, 40)
		progressRect = pygame.Rect(5, 705, width, 40)
		
		pygame.draw.rect(screen, (255, 255, 255), outerRect)
		pygame.draw.rect(screen, (200, 200, 200), innerRect)
		pygame.draw.rect(screen, playerColors[self.index], progressRect)
	
	def update(self, dx, dy, walls, players, shooter):	
		vx = 0
		vy = 0
		if self.used < self.movement:
			vx = dx * self.speed
			vy = dy * self.speed
			newCollCircle = Circle(playerRadius, self.collCircle.x + vx, self.collCircle.y + vy)
			
			for wall in walls:
				if not circleLine(newCollCircle, wall):
					continue
				else:
					return
				
			for player in players:
				if player is not shooter:
					if not circleCircle(newCollCircle, player.collCircle):
						continue
					else:
						return
		
			if newCollCircle.right < windowDim and newCollCircle.bottom < playHeight and newCollCircle.top > 0 and newCollCircle.left > 0:
				self.x += vx
				self.y += vy
				self.collCircle.set(self.x, self.y)
				self.rect.centerx = self.x
				self.rect.centery = self.y
				if vx is not 0 or vy is not 0:
					self.used += self.speed
	
	def start_turn(self):
		self.used = 0	
		self.shotTaken = False
		