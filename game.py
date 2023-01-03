
import pygame
import math

class Ship:
    def __init__(self, position):
        self.OriginalImage = pygame.image.load("Frigate3.png")
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
        

screen_size = [800,800]
window = pygame.display.set_mode(screen_size)

timer = pygame.time.Clock()
black = [0,0,0]

player = Ship([200,400])

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
                
    player.drawShip()
    pygame.display.flip()
    timer.tick(60)
