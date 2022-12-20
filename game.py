from pygame import *

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
        
    def collide(self):
        if self.rect.colliderect(player):
            
    def AsteroidTeleport(self, position):
        if self.position == 0:
            self.possition = 800        

class Ship:
    def __init__(self, position):
        self.shipImage = image.load("Frigate3.png")
        self.rect = window.blit(self.shipImage, [400,400])
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, [400,400])

screen_size = [800,800]
window = display.set_mode(screen_size)
         
timer = time.Clock()
black = [0,0,0]

player = Ship([400,400])

asteroid = Asteroid([25,25], 2)

while True:
    for event in event.get():
        if event.type == QUIT:
            quit = True
            quit()
            sys.exit(0)
    
    window.fill(black)
    player.drawShip()
    asteroid.drawAsteroid()
    display.flip()
    timer.tick(60)
    