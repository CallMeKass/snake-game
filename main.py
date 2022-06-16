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
snake_block=10

clock = pygame.time.Clock()
snake_speed=30

while run_game:
    for event in pygame.event.get():
        if debugger: print(event)
        if event.type==pygame.QUIT:
            run_game=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    x1 += x1_change
    y1 += y1_change

    dis.fill(white)
    pygame.draw.rect(dis,blue,[x1,y1,snake_block,snake_block])     

    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()
quit()
