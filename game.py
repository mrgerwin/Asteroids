from pygame import *

class Ship:
    def __init__(self, position):
        self.shipImage = image.load("Frigate3.png")
        self.rect = window.blit(self.shipImage, [400,400])
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, [400,400])
        
        
        
class Lasers:
    def __init__(self, position):
        self.Laserimage = image.load("LaserBeam.png")
        self.rect = window.blit(self.Laserimage,[100,100])
        
    def drawLaser(self):
        self.rect = window.blit(self.Laserimage, [100,100])

screen_size = [800,800]
window = display.set_mode(screen_size)

timer = time.Clock()
black = [0,0,0]

player = Ship([400,400])
Laser1 = Lasers([100,100])

while True:
    for event in event.get():
        if event.type == QUIT:
            quit = True
            quit()
            sys.exit(0)
    
    window.fill(black)
    player.drawShip()
    Laser1.drawLaser()
    display.flip()
    timer.tick(60)