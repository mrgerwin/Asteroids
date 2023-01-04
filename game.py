import pygame
from pygame import *
import math

class Ship:
    def __init__(self, position):
        self.OriginalImage = pygame.image.load("NewFrigate3.png")
        self.shipImage = self.OriginalImage
        self.position = position
        self.rect = window.blit(self.shipImage, self.position)
        self.angle = 0
        self.speed = 10
        
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, self.position)
        
    def rotate(self, angleDelta):
        self.angle += angleDelta
        originalPosition = self.position
        originalCenter = self.rect.center
        self.shipImage = pygame.transform.rotate(self.OriginalImage, self.angle)
        newRect = self.shipImage.get_rect()
        self.position = [originalCenter[0]-int(newRect.width/2), originalCenter[1]-int(newRect.height/2)]
        self.rect = window.blit(self.shipImage, self.position)
      
    def moveShip(self):
        print(math.cos((self.angle*math.pi)/180))
        self.position[0] += self.speed*math.cos((self.angle*math.pi)/180)  
        self.position[1] -= self.speed*math.sin((self.angle*math.pi)/180) 
class Ufo:
    def __init__(self, position):
        self.UfoImage = image.load("Ufo.png")
        self.rect = window.blit(self.UfoImage, [700,200])
    
    def drawUfo(self):
        self.rect = window.blit(self.UfoImage, [700,200])
class Background:
    def __init__(self,position):
        self.BgImage = image.load("Background.jpg")
        self.BgRect = window.blit(self.BgImage,[0,0])
    
    def drawBg(self):
        self.BgRect = window.blit(self.BgImage,[0,0])
    
screen_size = [800,800]
window = display.set_mode(screen_size)

#sound Attributes
mixer.init()
#theMusic = mixer.music.load("LeEpicBattleMusic.mp3")
theMusic = mixer.music.load("ChillPixelBackgroundMusic.mp3")

timer = time.Clock()
black = [0,0,0]

player = Ship([400,400])

enemy = Ufo([700,200])

Background = Background([0,0])

mixer.music.play(-1)

while True:
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rotate(5)
            if event.key == pygame.K_RIGHT:
                player.rotate(-5)
            if event.key == pygame.K_UP:
                player.moveShip()
    
    window.fill(black)
    Background.drawBg()
    player.drawShip()
    enemy.drawUfo()
    display.flip()
    timer.tick(60)