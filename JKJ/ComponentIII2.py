 #Krust Krew            
#RUN BILLY, RUN!!!!
#Kerien Washington,Jaden Moya,Jaylen Ovalles
#two sentence explanation of the game's objective

from gamelib import*#import game library

#objects and initial settings
game = Game (1600,830,"run billy run!!",60)
bk = Image("yo.jpg",game)
bk.resizeTo(game.width, game.height)
play= Image("play.png",game)
play.resizeTo(300,300)
play.moveTo(350,350)
sea = Image("sea.gif",game)
sea.resizeTo(game.width, game.height)
game.setBackground(sea)
billy = Animation("billy.png",12,game,332/6,152/2)
billy.moveTo(50,350)
over= Image("over.jpg",game)
over.resizeTo(game.width, game.height)
mouse.visible = False

mrkrabs = Animation("wolf.png",8,game,1200/2,1536/4)
mrkrabs.moveTo(50,350)
mrkrabs.resizeTo(200,150)
gems = Image("lollolo.png",game)
#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    play.draw()
    if mouse.LeftClick:
        game.over=True
    game.update(30)
game.over = False
#Level 1 - game loop
while not game.over:
    game.processInput()
    game.scrollBackground("left",10)
    gems.moveTo(mouse.x,mouse.y)
    if billy.collidedWith(mouse) and mouse.LeftClick:
        game.score += 35
    billy.draw()
    if mrkrabs.collidedWith(mouse) and mouse.LeftClick:
        game.score -= 45
    if keys.Pressed[K_a]:
        billy.x-=15
    if keys.Pressed[K_d]:
        billy.x+=15
    if keys.Pressed[K_w]:
        billy.y-=15
    if keys.Pressed[K_s]:
        billy.y+=15
    mrkrabs.draw()
   
    gems.draw()
    if keys.Pressed[K_LEFT]:
        mrkrabs.x-=15
    if keys.Pressed[K_RIGHT]:
        mrkrabs.x+=15
    if keys.Pressed[K_UP]:
        mrkrabs.y-=15
    if keys.Pressed[K_DOWN]:
        mrkrabs.y+=15
    if game.time <=0:
        game.over = True
    if game.score >= 700:
        game.over = True
        over.draw()
        
    game.displayTime(150,5)
    game.displayScore()
    game.update(30)
game.quit()


