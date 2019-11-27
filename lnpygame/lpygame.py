import pygame
from pygame.color import THECOLORS
import random
import time

pygame.init()
screen = pygame.display.set_mode([680,680])
screen.fill([255,255,255])

# myrect = pygame.Rect([300,300,120,200])
# pygame.draw.rect(screen,THECOLORS[list(THECOLORS.keys())[10]],myrect,2)

def create_rects(screen):
    for i in range(100):
        mycolor_index = random.choice(list(THECOLORS.keys()))
        mycolor = THECOLORS[mycolor_index]

        axis_x = random.randint(1,580)
        axis_y = random.randint(1,580)
        rect_width = random.randint(3,480)
        rect_height = random.randint(3,500)
        myrect = pygame.Rect([axis_x,axis_y,rect_width,rect_height])

        line_width = random.randint(2,5)

        pygame.draw.rect(screen, mycolor, myrect, line_width)

create_rects(screen)
pygame.display.flip()

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    time.sleep(1)

    screen.fill([255, 255, 255])
    create_rects(screen)
    pygame.display.flip()

pygame.quit()