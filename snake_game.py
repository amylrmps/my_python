import pygame, sys, random 
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)


pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()
# test_surface =  pygame.Surface((150,150))
#test_surface.fill((255,0,0))
# test_rect = pygame.Rect(30,24,100,100)
#test_rect =  test_surface.get_rect(topright = (300, 150))

# x_pos = 75
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((130,1,130))

    fruit.draw_fruit()
    snake.draw_snake()

    # pygame.draw.rect(screen, (0,255,0), test_rect)
    # x_pos += 1
    # if x_pos > 150:
    #     x_pos = 0

    #screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(60)
