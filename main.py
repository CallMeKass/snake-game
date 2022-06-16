import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
run_game=True
debugger=True
while run_game:
    for event in pygame.event.get():
        if debugger: print(event)
        if event.type==pygame.QUIT:
            run_game=False

pygame.quit()
quit()
