import pygame
import time
from pygame.locals  import *

def main():
    screen = pygame.display.set_mode((480,852),0,32)

    background = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/background.png")

    aircraft = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/hero1.png")

    x = 210
    y = 700

    while True:
        screen.blit(background, (0,0))

        screen.blit(aircraft,(x,y))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    x -=5
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    x +=5
                elif event.key == K_s or event.key == K_DOWN:
                    print("down")
                    y +=5
                elif event.key == K_w or event.key == K_UP:
                    print("up")
                    y -=5
                elif event.key == K_SPACE:
                    print("stop")
                    time.sleep(0.01)
                    flag = 0
                    while True:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN and event.key ==K_SPACE:
                                print("start")
                                flag = 1
                                break
                        if flag :
                            break

        time.sleep(0.01)

if __name__ == '__main__':
    main()