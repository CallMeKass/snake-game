from distutils.log import debug
import pygame
import time
pygame.init()

dis_width=800
dis_height=600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by CallMeKass')

blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)
black=(0,0,0)
 
snake_block=10
snake_speed=30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width/2)-70, (dis_height/2)-100])

def game_loop(debug_enabled=False) -> None:
    snake_x = int(dis_width/2)
    snake_y = int(dis_height/2)

    snake_xdelta = 0       
    snake_ydelta = 0

    run_game=True
    while run_game:
        for event in pygame.event.get():
            if debug_enabled: print(event)
            if event.type==pygame.QUIT:
                run_game=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_xdelta = -snake_block
                    snake_ydelta = 0
                elif event.key == pygame.K_RIGHT:
                    snake_xdelta = snake_block
                    snake_ydelta = 0
                elif event.key == pygame.K_UP:
                    snake_ydelta = -snake_block
                    snake_xdelta = 0
                elif event.key == pygame.K_DOWN:
                    snake_ydelta = snake_block
                    snake_xdelta = 0


        if snake_x >= dis_width or snake_x < 0 or snake_y >= dis_height or snake_y < 0:
            run_game = False

        snake_x += snake_xdelta
        snake_y += snake_ydelta

        dis.fill(white)
        pygame.draw.rect(dis,black,[snake_x,snake_y,snake_block,snake_block])     

        pygame.display.update()

        clock.tick(snake_speed)

    message("You lost",red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


game_loop()