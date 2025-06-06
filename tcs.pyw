import pygame
import sys
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        #创建一个矩形
        fruit_rect = pygame.Rect(self.x*cell_size,self.y*cell_size,
                    cell_size,cell_size)
        #绘制矩形
        pygame.draw.rect(window,(126,166,114),fruit_rect)
    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)

class SNAKE:
    def __init__(self):
        self.body=[Vector2(7,7),Vector2(6,7),Vector2(5,7)]
        self.draction=Vector2(1,0)
        self.new_block=False

    def draw_snake(self):
        for black in self.body:
            pos_x=black[0]*cell_size
            pos_y=black[1]*cell_size
            snake_rect=pygame.Rect(pos_x,pos_y,cell_size,cell_size)
            pygame.draw.rect(window,(126,166,114),snake_rect)
    def move_snake(self):
        if self.new_block==False:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.draction)
            self.body=body_copy[:]
        else:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.draction)
            self.body=body_copy[:]
            self.new_block=False
    def add_block(self):
        self.new_block=True
class MAIN:
    def __init__(self):
        self.fruit = FRUIT()
        self.snake=SNAKE()
    def update(self):
        self.snake.move_snake()
        self.check_collement()
        self.check_fail()
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
    def check_collement(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    def check_fail(self):
        if not(0<=self.snake.body[0].x<cell_number) or not(0<=self.snake.body[0].x<cell_number):
            self.game_over()
        for block in self.snake.body[1:]:
            if self.snake.body[0]==block:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
    




pygame.init()
cell_size = 10
cell_number = 74
window = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
pygame.display.set_caption("我的第一个游戏")
clock=pygame.time.Clock()
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#实例化对象
main=MAIN()
while True:
    for event in pygame.event.get():
        if event.type == SCREEN_UPDATE:
            main.update()
        if event.type == pygame.QUIT:
            main.game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.draction.y!=1:
                    main.snake.draction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main.snake.draction.y!=-1:
                    main.snake.draction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main.snake.draction.x!=1:
                    main.snake.draction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main.snake.draction.x!=-1:
                    main.snake.draction = Vector2(1,0)
    window.fill((175,245,70))
    main.draw_elements()
    pygame.display.update()