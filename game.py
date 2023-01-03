from pygame import *

class Ship:
    def __init__(self, position):
        self.shipImage = image.load("NewFrigate3.png")
        self.rect = window.blit(self.shipImage, [400,400])
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, [400,400])
class Background:
    def __init__(self,position):
        self.BgImage = image.load("Background.jpg")
        self.BgRect = window.blit(self.BgImage,[0,0])
    
    def drawBg(self):
        self.BgRect = window.blit(self.BgImage,[0,0])
    
screen_size = [800,800]
window = display.set_mode(screen_size)

#sound Attributes
mixer.init()
#theMusic = mixer.music.load("LeEpicBattleMusic.mp3")
theMusic = mixer.music.load("ChillPixelBackgroundMusic.mp3")

timer = time.Clock()
black = [0,0,0]

player = Ship([400,400])

Background = Background([0,0])

mixer.music.play(-1)

while True:
    for event in event.get():
        if event.type == QUIT:
            quit = True
            quit()
            sys.exit(0)
    
    window.fill(black)
    Background.drawBg()
    player.drawShip()
    display.flip()
    timer.tick(60)