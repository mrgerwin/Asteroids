import pygame 
import random

class Asteroid:
    def __init__(self, position, size, speed):
        self.position = position
        self.size = size
        self.speed = speed
        self.AsteroidImage = pygame.image.load("Asteroid.png")
        self.AsteroidImage = pygame.transform.rotozoom(self.AsteroidImage, 0, .15)

        
    def drawAsteroid(self):
        self.rect = window.blit(self.AsteroidImage, self.position)
        
    def AsteroidMove(self):
        print(self.position)
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        
    def Split(self):
        if self.rect.colliderect(Laser):
            self.size -= 1
            if self.size == 0:
                asteroids.remove(self)
        
    def collide(self):
        if self.rect.colliderect(player):
            pass
            
            
    def AsteroidTeleport(self):
        if self.position[0] <= -151:
            self.position[0] = 800
        if self.position[0] >= 801:
            self.position[0] = -150
        if self.position[1] <= -151:
            self.position[1] = 800
        if self.position[1] >= 801:
            self.position[1] = -150

class Ship:
    def __init__(self, position):
        self.position = position
        self.shipImage = pygame.image.load("Frigate3.png")
        self.rect = window.blit(self.shipImage, self.position)
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, self.position)
        
    def moveShip(self):
        self.position[0] += 1
        

screen_size = [800,800]
window = pygame.display.set_mode(screen_size)

AsteroidSpeeds = [[0,1],[0,2],[0,3],[1,1], [1,2], [1,3], [-1, 1], [-1, 2], [-1, 3], [2, 1], [2, 2], [2, 3], [-2, 1], [-2, 2], [-2, 3]]
SpeedX = 0
SpeedY = 0
topScreen = 0
bottomScreen = 0
leftScreen = 0
rightScreen = 0
timer = pygame.time.Clock()
black = [0,0,0]

player = Ship([400,400])
Asteroid1 = Asteroid([100,100], 3, random.choice(AsteroidSpeeds))
asteroids = [Asteroid1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.moveShip()
            drawShip
            quit = True
            quit()
            sys.exit(0)
    
    window.fill(black)
    player.drawShip()
    player.moveShip()
    for asteroid in asteroids:
        asteroid.AsteroidMove()
        asteroid.drawAsteroid()
        asteroid.AsteroidTeleport()
    pygame.display.flip()
    timer.tick(60)
    