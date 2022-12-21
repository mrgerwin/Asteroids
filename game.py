import pygame 

class Asteroid:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.AsteroidImage = image.load("Asteroid.png")
        
    def drawAsteroid(self):
        self.rect = window.blit(self.AsteroidImage, self.position)
        
    def Split():
        if self.rect.colliderect(Laser):
            self.size -= 1
            if self.size == 0:
                asteroids.remove(self)
        
    def collide(self):
        if self.rect.colliderect(player):
            pass
            
            
    def AsteroidTeleport(self, position):
        if self.position == 0:
            self.position = 800

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

asteroid1 = 
topScreen = 0
bottomScreen = 0
leftScreen = 0
rightScreen = 0
timer = pygame.time.Clock()
black = [0,0,0]

player = Ship([400,400])

asteroids = []

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
        asteroid.drawAsteroid()
    pygame.display.flip()
    timer.tick(60)
    