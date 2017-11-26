import pygame
from math import atan2, sin, cos
from utility.Circle import Circle
from utility.Collision import *
from utility.Constants import windowDim, playHeight, bounceSound, hitSound, loadImage

class Bullet (pygame.sprite.Sprite):
	
	radius = 10
	maxHits = hits = 3
	kill = False
	charge = -4
	speed = 5
	
	def __init__(self, pos, angle, index):
		pygame.sprite.Sprite.__init__(self)
		
		self.image, self.rect = loadImage("Disc" + str(index) + ".png")

		self.rect.center = pos
		self.x, self.y = pos
	
		self.collCircle = Circle(self.radius, self.x, self.y)
		
		self.vx = self.speed * cos(angle)
		self.vy = self.speed * sin(angle)
		
	def update(self, magnets):
		if self.hits < 0:
			self.kill = True
			return
		
		#Negative = repel, positive = attract
		for magnet in magnets:
			mvx, mvy = magnet.forceVector(self.collCircle, self.charge)
			self.vx += mvx
			self.vy += mvy
			
		self.x += self.vx
		self.y += self.vy

		if self.x > windowDim:
			self.x -= windowDim
		elif self.x < 0:
			self.x += windowDim
		
		if self.y > playHeight:
			self.y -= playHeight
		elif self.y < 0:
			self.y += playHeight
		
		self.rect.centerx = self.collCircle.x = self.x
		self.rect.centery = self.collCircle.y = self.y
			
	def collide(self, walls, players, magnets, shooter):
		nextCircle = Circle(self.radius, self.x + self.vx, self.y + self.vy)
		
		for magnet in magnets:
			if circleCircle(nextCircle, magnet.collCircle):
				if self.hits > 0:
					bounceSound.play()
					self.vx, self.vy = self.circleReflectDirection(magnet.collCircle)
				self.hits -= 1
		
		for wall in walls:
			if circleLine(nextCircle, wall):
				if self.hits > 0:
					bounceSound.play()
					self.vx, self.vy = self.wallReflectDirection(wall.getAngle())
				self.hits -= 1
		
		#Make sure this works
		for player in players:
			if player is not shooter:
				if circleCircle(self.collCircle, player.collCircle):
					if self.hits is not self.maxHits:
						hitSound.play()
						self.hits = -1
						player.dead = True
					else:
						bounceSound.play()
						self.hits -= 1
						self.vx, self.vy = self.circleReflectDirection(player.collCircle)
	
	def wallReflectDirection(self, wallAngle):
		speed = sqrt(self.vx * self.vx + self.vy * self.vy)
		angle = atan2(self.vy, self.vx)
		da = wallAngle - angle
		vx = speed * cos(angle + 2 * da)
		vy = speed * sin(angle + 2 * da)
		return vx, vy
	
	def circleReflectDirection(self, c):
		dx = c.x - self.x
		dy = c.y - self.y
		
		mag = sqrt(dx * dx + dy * dy)
		
		dx /= mag
		dy /= mag
		
		dp = self.vx * dx + self.vy * dy
		
		return self.vx - 2 * dp * dx, self.vy - 2 * dp * dy
		
		
		
		