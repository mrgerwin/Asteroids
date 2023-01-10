import math
import pygame 
import random

def drawText():
    global Text, white
    thewordsthatiuseText = Text.render("OBJECTIVE: DESTROY THE METEORS", True, white)
    
    window.blit(thewordsthatiuseText, (130, 20))

def drawScore():
    global score, white
    controlText = Text.render("SPACE = Shoot         Up/Down Arrow to Move", True, white)
    
    window.blit(controlText, (35, 700))

def Split():
    NumOfAst = random.randint(2,4)
    for i in range(NumOfAst):
        NewAst = Asteroid([Asteroid1.position[0], Asteroid1.position[1]] , Asteroid1.size-1, random.choice(AsteroidSpeeds))
        asteroids.append(NewAst)
    asteroids.remove(Asteroid1)
    
class Asteroid:
    def __init__(self, position, size, speed):
        self.position = position
        self.size = size
        self.speed = speed
        self.AsteroidImage = pygame.image.load("Asteroid.png")
        self.AsteroidImage = pygame.transform.rotozoom(self.AsteroidImage, 0, self.size*.05)

        
    def drawAsteroid(self):
        self.rect = window.blit(self.AsteroidImage, self.position)
        
    def AsteroidMove(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        
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
        self.OriginalImage = pygame.image.load("NewFrigate3.png")
        self.shipImage = self.OriginalImage
        self.position = position
        self.rect = window.blit(self.shipImage, self.position)
        self.angle = 0
        self.speed = 0
        self.TurnSpeed = 0
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, self.position)
        
    def rotate(self):
        self.angle += self.TurnSpeed
        originalPosition = self.position
        originalCenter = self.rect.center
        self.shipImage = pygame.transform.rotate(self.OriginalImage, self.angle)
        newRect = self.shipImage.get_rect()
        self.position = [originalCenter[0]-int(newRect.width/2), originalCenter[1]-int(newRect.height/2)]
        print(self.position)
        self.rect = window.blit(self.shipImage, self.position)
     
    def moveShip(self):
        #print(self.position)
        self.position[0] += self.speed*math.cos((self.angle*math.pi)/180)  
        self.position[1] -= self.speed*math.sin((self.angle*math.pi)/180)
    
    def shipDeath(self):
        print ("you died")
        exsploshinImage=pygame.image.load("C:/Users/Student/Documents/GitHub/Asteroids/images-removebg-preview.png")
        window.blit(exsploshinImage, self.position)
        self.position = [200,400]
        self.rect = window.blit(self.shipImage, self.position)
        #print(self.position)
        

  
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

AsteroidSpeeds = [[0,1],[0,2],[0,3],[1,1], [1,2], [1,3], [-1, 1], [-1, 2], [-1, 3], [2, 1], [2, 2], [2, 3], [-2, 1], [-2, 2], [-2, 3]]

timer = pygame.time.Clock()
black = [0 ,0,0]
white = [255, 255, 255]
player = Ship([200,400])

lasers = []

#sound Attributes
pygame.mixer.init()
#theMusic = mixer.music.load("LeEpicBattleMusic.mp3")
theMusic = pygame.mixer.music.load("ChillPixelBackgroundMusic.mp3")


#these spaceness things
pygame.font.init()
Text = pygame.font.SysFont("consolas", 30)
player = Ship([200,400])
Asteroid1 = Asteroid([100,100], 3, random.choice(AsteroidSpeeds))
asteroids = [Asteroid1]
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
                #print("Pressed space")
                #print(player.position)
                Laser1 = Lasers(player.position, player.angle)
                lasers.append(Laser1) 
            if event.key == pygame.K_LEFT:
                player.TurnSpeed=4
                #print(player.TurnSpeed)
            if event.key == pygame.K_RIGHT:
                player.TurnSpeed=-4
                #print(player.TurnSpeed)
            if event.key == pygame.K_UP:
                player.speed = 4
            if event.key == pygame.K_y:
                #print("Y")
                Split()
            if event.key == pygame.K_m:
                for astroid in asteroids:
                    print(str(astroid.speed) +  '  ' + str(astroid.position))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speed =0
            if event.key == pygame.K_LEFT:
                player.TurnSpeed=0
            if event.key == pygame.K_RIGHT:
                player.TurnSpeed=0
    window.fill(black)
    Background.drawBg()
    enemy.drawUfo()
    player.rotate()
    player.moveShip()
    player.drawShip()
    player.moveShip()
    for asteroid in asteroids:
        asteroid.AsteroidMove()
        asteroid.drawAsteroid()
        asteroid.AsteroidTeleport()
        if player.rect.colliderect(asteroid.rect):
            player.shipDeath()
            
    drawText()
    drawScore()

    for laser in lasers:
        laser.Shoot()
        laser.drawLaser()
    pygame.display.flip()
    timer.tick(60)


