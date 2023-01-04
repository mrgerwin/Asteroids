import pygame
import math

class Ship:
    def __init__(self, position):
        self.shipImage = pygame.image.load("Frigate3.png")
        self.rect = window.blit(self.shipImage, [400,400])
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, [400,400])
        
        
        
class Lasers:
    def __init__(self, position, angle):
        self.position = position
        self.Laserimage = pygame.image.load("LaserBeam.png")
        self.angle = angle
        
        self.Laserimage = pygame.transform.rotate(self.Laserimage, self.angle)
        self.rect = window.blit(self.Laserimage,self.position)
        
    def drawLaser(self):
        self.rect = window.blit(self.Laserimage, self.position)
        
    
    
    def rotate(self, angle):
        self.Laserimage = pygame.transform.rotate(self.OriginalImage, self.angle)
    
    def Shoot(self):
        self.position[0]+= math.cos((self.angle*math.pi)/180)
        self.position[1]-= math.sin((self.angle*math.pi)/180)

screen_size = [800,800]
window = pygame.display.set_mode(screen_size)

timer = pygame.time.Clock()
black = [0 ,0,0]

player = Ship([400,400])
lasers = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            pygame.quit()
            sys.exit(0)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Pressed space")
                Laser1 = Lasers([100,100], 45)
                lasers.append(Laser1) 
                
            
    
    window.fill(black)
    player.drawShip()
    for laser in lasers:
        laser.Shoot()
        laser.drawLaser()
    pygame.display.flip()
    timer.tick(60)