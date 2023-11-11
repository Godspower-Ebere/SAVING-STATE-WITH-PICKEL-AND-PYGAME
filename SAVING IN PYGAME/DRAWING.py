import pygame
import pickle
pygame.init()
size=width,height=(1000,800)
screen=pygame.display.set_mode(size)
load=open("save.game","rb")
o=pickle.load(load)
draw=o
draw2=[]

run=True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            data=open("save.game","wb")
            pickle.dump(draw,data)
            run=False
    mou=pygame.mouse.get_pressed()
    pos=pygame.mouse.get_pos()
    x,y=pos
    if mou[0]:
        draw.append([x-10,y-10,(255,255,255)])
    if mou[2]:
        draw2.append([x-10,y-10,(0,0,0)])
    for i in draw:
        wr=pygame.Rect(i[0],i[1],20,20)
        pygame.draw.rect(screen,(i[2]),wr)
##        if mou[2]:
##            for i in draw2:
##                br=pygame.Rect(i[0],i[1],20,20)
##                if wr.colliderect(br):
##                    print("yes")
        if mou[0]:
            for i in draw2:
                br=pygame.Rect(i[0],i[1],20,20)
                if wr.colliderect(br):
                    i[2]=(255,255,255)
        
    for i in draw2:
        pygame.draw.rect(screen,(i[2]),(i[0],i[1],20,20))
    pygame.display.update()
pygame.quit()
