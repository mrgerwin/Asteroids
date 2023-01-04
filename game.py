import pygame
import math

def drawText():
    global Text, white
    thewordsthatiuseText = Text.render("OBJECTIVE: DESTROY THE METEORS", True, white)
    
    window.blit(thewordsthatiuseText, (130, 20))

def drawScore():
    global score, white
    controlText = Text.render("SPACE = Shoot         Up/Down Arrow to Move", True, white)
    
    window.blit(controlText, (35, 700))

class Ship:
    def __init__(self, position):
        self.OriginalImage = pygame.image.load("NewFrigate3.png")
        self.shipImage = self.OriginalImage
        self.position = position
        self.rect = window.blit(self.shipImage, self.position)
        self.angle = 0

        self.speed = 0
        
    
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
       
class Lasers:
    def __init__(self, position, angle):
        self.position = position
        self.Originalimg = pygame.image.load("LaserBeam.png")
        self.angle = angle
        self.Laserimage = self.Originalimg
        #self.Laserimage = pygame.transform.rotate(self.Laserimage, self.angle)
        
        self.rect = window.blit(self.Laserimage,self.position)
        self.newRect = ""
        self.originalCenter = ""
        self.originalPosition = ""
        self.rotate()
        
    def drawLaser(self):
        self.rect = window.blit(self.Laserimage, self.position)
        
    
    
    def rotate(self):
        self.originalPosition = self.position
        self.originalCenter = self.rect.center
        self.Laserimage = pygame.transform.rotate(self.Originalimg, self.angle)
        self.newRect = self.Laserimage.get_rect()
        self.position = [self.originalCenter[0] -int(self.newRect.width/2), self.originalCenter[1] -int(self.newRect.height/2)]
    
    def Shoot(self):
        self.position[0]+= math.cos((self.angle*math.pi)/180)
        self.position[1]-= math.sin((self.angle*math.pi)/180)
        #print(self.position)
class Ufo:
    def __init__(self, position):
        self.UfoImage = pygame.image.load("Ufo.png")
        self.rect = window.blit(self.UfoImage, [700,200])
    
    def drawUfo(self):
        self.rect = window.blit(self.UfoImage, [700,200])
class Background:
    def __init__(self,position):
        self.BgImage = pygame.image.load("Background.jpg")
        self.BgRect = window.blit(self.BgImage,[0,0])
    
    def drawBg(self):
        self.BgRect = window.blit(self.BgImage,[0,0])
        
screen_size = [800,800]
window = pygame.display.set_mode(screen_size)

screen_size = [800,800]
window = pygame.display.set_mode(screen_size)

timer = pygame.time.Clock()
black = [0 ,0,0]
player = Ship([200,400])

lasers = []

#sound Attributes
pygame.mixer.init()
#theMusic = mixer.music.load("LeEpicBattleMusic.mp3")
theMusic = pygame.mixer.music.load("ChillPixelBackgroundMusic.mp3")


timer = pygame.time.Clock()
black = [0,0,0]
white = [255, 255, 255]


#these spaceness things
font.init()
Text = font.SysFont("consolas", 30)
player = Ship([200,400])

enemy = Ufo([700,200])

Background = Background([0,0])

pygame.mixer.music.play(-1)

while True:
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Pressed space")
                print(player.position)
                Laser1 = Lasers(player.position, player.angle)
                lasers.append(Laser1) 
            if event.key == pygame.K_LEFT:
                player.rotate(5)
            if event.key == pygame.K_RIGHT:
                player.rotate(-5)
            if event.key == pygame.K_UP:
                player.speed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speed =0
                

    window.fill(black)
    Background.drawBg()
    enemy.drawUfo()
    player.moveShip()
    player.drawShip()

    drawText()
    drawScore()



    for laser in lasers:
        laser.Shoot()
        laser.drawLaser()
    pygame.display.flip()
    timer.tick(60)

