import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption('Snake game by CallMeKass')

blue=(0,0,255)
red=(255,0,0)

run_game=True
debugger=True

while run_game:
    for event in pygame.event.get():
        if debugger: print(event)
        if event.type==pygame.QUIT:
            run_game=False
    pygame.draw.rect(dis,blue,[200,150,10,10])     
    pygame.display.update()

pygame.quit()
quit()
