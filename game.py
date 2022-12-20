from pygame import *

class Asteroid:
    def __init__(self, position, size):
        self.position = position
        self.size = size
<<<<<<< HEAD
        self.AsteroidImage = image.load("Atseroid.jpg")
        pass
=======
        self.AsteroidImage = image.load("Asteroid.jpeg")
>>>>>>> 1f83e06884a05f27de55605e8b6403734257c1d1
        
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
    