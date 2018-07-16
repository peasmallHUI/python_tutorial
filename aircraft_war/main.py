import pygame
import time
import random
from pygame.locals  import *

class BaseCraft(object):
    def __init__(self,screen_temp,x,y,image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.screen_temp = screen_temp
        self.bullet_list = []

    def display(self):
        self.screen_temp.blit(self.image, (self.x,self.y))
        for bullet in self.bullet_list:
            self.screen_temp.blit(bullet.image, (bullet.x,bullet.y))
            bullet.move()
            if bullet.judge() :
                self.bullet_list.remove(bullet) 
            
    def fire(self,bullet_class):
        if bullet_class == Bullet:
            bullet = bullet_class(self.screen_temp,self.x,self.y)
            self.bullet_list.append(bullet)
        elif bullet_class == EnemyBullet:
            ran = random.randint(1,100)
            if ran == 1 or ran == 2:
                bullet = bullet_class(self.screen_temp,self.x,self.y)
                self.bullet_list.append(bullet)

class AirCraft(BaseCraft):
    def __init__(self,screen_temp):
        BaseCraft.__init__(self,screen_temp,210,700,"e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/hero1.png")
        # self.x = 210
        # self.y = 700
        # self.image = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/hero1.png")
        # self.screen_temp = screen_temp
        # self.bullet_list = []
    
    # def display(self):
    #     self.screen_temp.blit(self.image, (self.x,self.y))
    #     for bullet in self.bullet_list:
    #         self.screen_temp.blit(bullet.image, (bullet.x,bullet.y))
    #         bullet.move()
    #         if bullet.judge() :
    #             self.bullet_list.remove(bullet)         
    
    # def fire(self):
    #     bullet = Bullet(self.screen_temp,self.x,self.y)
    #     self.bullet_list.append(bullet)
    
    def move_x(self,x):
        self.x += x

    def move_y(self, y):
        self.y += y

class EnemyCraft(BaseCraft):
    def __init__(self,screen_temp):
        # self.x = 0
        # self.y = 0
        # self.image = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/enemy0.png")
        # self.screen_temp = screen_temp
        # self.bullet_list = []
        BaseCraft.__init__(self,screen_temp,0,0,"e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/enemy0.png")
        self.direction = "right"
    
    # def display(self):
    #     self.screen_temp.blit(self.image, (self.x,self.y))
    #     for bullet in self.bullet_list:
    #         self.screen_temp.blit(bullet.image, (bullet.x,bullet.y))
    #         bullet.move()
    #         if bullet.judge() :
    #             self.bullet_list.remove(bullet)   
    
    # def fire(self):
    #     bullet = Bullet(self.screen_temp,self.x,self.y)
    #     self.bullet_list.append(bullet)
    
    def move(self):
        if self.direction == "right":
            self.x +=5
        elif self.direction == "left":
            self.x -=5
        
        if self.x > 480-50 :
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
    
    # def move_x(self,x):
    #     self.x += x
    
    # def move_y(self, y):
    #     self.y += y

class BaseBullet(object):
    def __init__(self,screen_temp,x,y,image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.screen = screen_temp

class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self, screen_temp, x+40, y+20, "e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/bullet.png")
        # self.x = x + 40
        # self.y = y + 20
        # self.image = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/bullet.png")
        # self.screen = screen_temp
    
    def move(self):
        self.y -=5
    
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/bullet1.png")
        # self.x = x + 25
        # self.y = y + 40
        # self.image = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/bullet1.png")
        # self.screen = screen_temp
    
    def move(self):
        self.y +=5
    
    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


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
                    aircraft_temp.fire(Bullet)

                elif event.key == K_ESCAPE:
                    print("stop")
                    time.sleep(0.01)
                    flag = 0
                    while True:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN and event.key ==K_ESCAPE:
                                print("start")
                                flag = 1
                                break
                        if flag :
                            break


def main():
    # window
    screen = pygame.display.set_mode((480,852),0,32)
    
    #background
    background = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/background.png")
    
    #aircraft
    aircraft = AirCraft(screen)
    # aircraft = pygame.image.load("e:/Documents/GitHub/python_tutorial/aircraft_war/feiji/hero1.png")
    # x = 210
    # y = 700

    #enemy
    enemy = EnemyCraft(screen)

    while True:
        screen.blit(background, (0,0))
        # screen.blit(aircraft,(x,y))
        aircraft.display()
        enemy.display()
        enemy.move()
        enemy.fire(EnemyBullet)
        pygame.display.update()
        key_control(screen,aircraft)        
        time.sleep(0.01)

if __name__ == '__main__':
    main()