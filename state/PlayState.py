import pygame
import math
from main.StateManager import getManager
from state.GameState import GameState
from entity.Bullet import Bullet
from entity.Player import Player
from utility.Image import Image
from pygame.locals import *
from random import randint
from utility.Constants import windowDim, playHeight, loadSound, loadWalls, loadImage, loadMagnets

class PlayState(GameState):
    
    playerIndex = 0
    gameOver = False
    
    def __init__(self, playerNum):
        
        self.uiSprites = pygame.sprite.RenderPlain()
        
        #Initialize Players
        self.players = pygame.sprite.RenderPlain()
        
        for i in range(0, playerNum):
            self.players.add(Player(i))
    
        self.player = self.players.sprites()[0]
        self.totalPlayers = playerNum
        
        #Initialize Bullets
        self.bullets = pygame.sprite.RenderPlain()
        
        #Map Selection
        mapNum = (randint(1, 3))
            
        #Initialize Magnets
        self.magnets = loadMagnets("magnets" + str(mapNum) + ".txt")
        
        #Initialize Walls
        self.walls = loadWalls("BaseMap.txt")
        for wall in loadWalls("walls" + str(mapNum) + ".txt"):
            self.walls.append(wall)
            
        #Initialize Sounds
        self.shootSound = loadSound("Shoot.wav")
    
    def update(self):
        if self.gameOver:
            pygame.time.wait(3000)
            getManager().pop()
        
        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if not self.player.shotTaken:
                        self.shoot()
                        self.player.shotTaken = True
            if event.type == QUIT:
                return False
        
        keys = pygame.key.get_pressed()
        
        dx = dy = 0
        if keys[K_UP] or keys[K_w]:
            dy = -1
        elif keys[K_DOWN] or keys[K_s]:
            dy = 1
                
        if keys[K_RIGHT] or keys[K_d]:
            dx = 1
        elif keys[K_LEFT] or keys[K_a]:
            dx = -1
            
        if math.fabs(dx) == 1.0 and math.fabs(dy) == 1.0:
            dx *= math.sqrt(2) / 2
            dy *= math.sqrt(2) / 2 
        
        #Update Bullet
        for bullet in self.bullets:
            bullet.collide(self.walls, self.players, self.magnets, self.player)
            bullet.update(self.magnets)
            if bullet.kill:
                self.bullets.remove(bullet)
        
        #Update Players
        for player in self.players:
            if player is not self.player:
                if player.dead:
                    self.players.remove(player)
                    self.totalPlayers -= 1
                    if player.index < self.playerIndex:
                        self.playerIndex -= 1
            else:
                player.update(dx, dy, self.walls, self.players, player)
                
        #End Turn
        if self.player.shotTaken and self.bullets.__len__() is 0:
            self.end_turn()
            
        #End Game
        if self.players.__len__() is 1:
            self.gameOver = True
        
        return True
            
    def render(self, screen):
        self.players.draw(screen)
        self.magnets.draw(screen)
        self.player.render(screen)
        self.bullets.draw(screen)
        for wall in self.walls: 
            pygame.draw.line(screen, (255, 255, 255), wall.p1, wall.p2)
        if self.gameOver:
            self.printWinner()
            self.uiSprites.draw(screen)
                
    def end_turn(self):
        self.playerIndex = (self.playerIndex + 1) % self.totalPlayers
        self.player = self.players.sprites()[self.playerIndex]       
        self.player.start_turn()
        
    def shoot(self):
        self.shootSound.play()
        playerX = self.player.rect.centerx
        playerY = self.player.rect.centery
        
        mousePos = pygame.mouse.get_pos()
        
        dx = float(mousePos[0] - playerX)
        dy = float(mousePos[1] - playerY)
        
        if dy != 0:
            angle = math.atan2(dy, dx)
        else:
            if dx > 0:
                angle = 0
            else:
                angle = math.pi
        
        self.bullets.add(Bullet((playerX, playerY), angle, self.player.index))
        
    def printWinner(self):
        survivor = self.players.sprites()[0]
        textImage, textRect = loadImage("Player" + str(survivor.index + 1) + "Wins.png")
        textRect.center = (windowDim / 2, playHeight / 2)
        winnerText = Image(textImage, textRect)
        self.uiSprites.add(winnerText)
            
        
        