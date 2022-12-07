import pygame as g
import time
def cartoon():
    g.init()
    s=600,400
    screen=g.display.set_mode(s)
    i=1
    while 1:
        for e in g.event.get():
            if e.type==g.QUIT:
                exit()
        image=g.image.load('./cartoon/'+str(i)+'.jpg')
        if i >= 2:
            i=1
        else:
            i=i+1
        screen.blit(image,(0,0))
        time.sleep(1/4)
        g.display.update()
