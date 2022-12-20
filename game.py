from pygame import *

class Asteroid:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.AsteroidImage = image.load("Asteroid.jpeg")
        pass
        
    def drawAsteroid(self):
        self.rect = window.blit(self.AsteroidImage, self.position)

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

while True:
    for event in event.get():
        if event.type == QUIT:
            quit = True
            quit()
            sys.exit(0)
    
    window.fill(black)
    player.drawShip()
    display.flip()
    timer.tick(60)
    