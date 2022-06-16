import pygame
pygame.init()

dis=pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake game by CallMeKass')

blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)

run_game=True
debugger=True

x1 = 400
y1 = 300
 
x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()

while run_game:
    for event in pygame.event.get():
        if debugger: print(event)
        if event.type==pygame.QUIT:
            run_game=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change

    dis.fill(white)
    pygame.draw.rect(dis,blue,[x1,y1,10,10])     

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
