import pygame
pygame.init()


dis_width=800
dis_height=600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by CallMeKass')

blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)

run_game=True
debugger=True

x1 = int(dis_width/2)
y1 = int(dis_height/2)
 
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
