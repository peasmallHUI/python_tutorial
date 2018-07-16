import pygame
import time
from pygame.locals  import *

class Aircraft(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.image = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/hero1.png")
        self.screen_temp = screen_temp
        self.bullet_list = []
    
    def display(self):
        self.screen_temp.blit(self.image, (self.x,self.y))

        for bullet in self.bullet_list:
            self.screen_temp.blit(bullet.image, (bullet.x,bullet.y))
            bullet.move()
    
    def fire(self):
        bullet = Bullet(self.screen_temp,self.x,self.y)
        self.bullet_list.append(bullet)
    
    def move_x(self,x):
        self.x += x
    
    def move_y(self, y):
        self.y += y

class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y + 20
        self.image = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/bullet.png")
        self.screen = screen_temp
    
    def move(self):
        self.y -=5

def key_control(screen_temp,aircraft_temp):
    for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    aircraft_temp.move_x(-5)
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    aircraft_temp.move_x(+5)
                elif event.key == K_s or event.key == K_DOWN:
                    print("down")
                    aircraft_temp.move_y(+5)
                elif event.key == K_w or event.key == K_UP:
                    print("up")
                    aircraft_temp.move_y(-5)
                elif event.key == K_SPACE:
                    print("fire")
                    aircraft_temp.fire()

                # elif event.key == K_ESCAPE:
                #     print("stop")
                #     time.sleep(0.01)
                #     flag = 0
                #     while True:
                #         for event in pygame.event.get():
                #             if event.type == KEYDOWN and event.key ==K_ESCAPE:
                #                 print("start")
                #                 flag = 1
                #                 break
                #         if flag :
                #             break


def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/background.png")
    aircraft = Aircraft(screen)
    # aircraft = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/hero1.png")
    # x = 210
    # y = 700

    while True:
        screen.blit(background, (0,0))
        # screen.blit(aircraft,(x,y))
        aircraft.display()
        pygame.display.update()
        key_control(screen,aircraft)        
        time.sleep(0.01)

if __name__ == '__main__':
    main()