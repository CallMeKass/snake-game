from distutils.log import debug
import pygame
import time
import random
pygame.init()

dis_width=800
dis_height=600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by CallMeKass')

blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)
black=(0,0,0)
green = (0, 255, 0)
yellow = (255, 255, 102)

 
snake_block=10
snake_speed=10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width/2)-70, (dis_height/2)-100])

def place_food():
    x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    return x,y

def game_loop(debug_enabled=False) -> None:
    snake_x = int(dis_width/2)
    snake_y = int(dis_height/2)

    snake_xdelta = 0       
    snake_ydelta = 0

    snake_List = []
    Length_of_snake = 1

    foodx,foody=place_food()

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
        pygame.draw.rect(dis,blue,[foodx,foody,snake_block,snake_block]) 

        snake_Head = []
        snake_Head.append(snake_x)
        snake_Head.append(snake_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        our_snake(snake_block, snake_List)
    
        pygame.display.update()
        if snake_x==foodx and snake_y==foody:
            foodx,foody=place_food()
            Length_of_snake += 1

        clock.tick(snake_speed)

    message("You lost",red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


game_loop()