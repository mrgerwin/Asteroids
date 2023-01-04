from pygame import *

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
        self.shipImage = image.load("Frigate3.png")
        self.rect = window.blit(self.shipImage, [400,400])
    
    def drawShip(self):
        self.rect = window.blit(self.shipImage, [400,400])

screen_size = [800,800]
window = display.set_mode(screen_size)

timer = time.Clock()
black = [0,0,0]
white = [255, 255, 255]

player = Ship([400,400])
#these spaceness things
font.init()
Text = font.SysFont("consolas", 30)

while True:
    for event in event.get():
        if event.type == QUIT:
            quit = True
            quit()
            sys.exit(0)
            

    
    window.fill(black)
    player.drawShip()
    drawText()
    drawScore()
    display.flip()
    timer.tick(60)