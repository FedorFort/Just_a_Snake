import random
import pygame
from food import Food

pygame.init()

WIDTH = 900
HEIGHT = 900
FPS = 40
HEAD_SIZE = 50

BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Snake():
    
    def __init__(self, screen_width, screen_height, head_size):
        x = random.randint(0, screen_width - head_size)
        y = random.randint(0, screen_height - head_size)
        self.head = pygame.Rect(x, y, head_size, head_size)
        self.body: list[pygame.Rect] = []
        self.body = []
        self.body_size = int(head_size * 0.8)
        self.dx = 0
        self.dy = 0
        self.speed = 5
        self.color = (100, 200, 100)
        
    def draw_head(self, screen):
        pygame.draw.rect(screen, self.color, self.head)

    def draw_body(self, screen: pygame.Surface):
        for piece in self.body:
            pygame.draw.rect(screen, self.color, piece)
        
    def move_head(self):
        self.head.x += self.dx * self.speed
        self.head.y += self.dy * self.speed

    def move_body(self):
        if self.body:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].center = self.body[i - 1].center
            self.body[0].center = self.head.center

    def change_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.dy != 1:
                self.dx = 0
                self.dy = -1
        elif keys[pygame.K_a]:
            if self.dx != 1:
                self.dx = -1
                self.dy = 0
        elif keys[pygame.K_s]:
            if self.dy != -1:
                self.dx = 0
                self.dy = 1
        elif keys[pygame.K_d]:
            if self.dx != -1:
                self.dx = 1
                self.dy = 0

    def grow(self):
        new = pygame.Rect(*self.head.center, self.body_size, self.body_size)
        new.center = self.head.center
        self.body.append(new)

    def draw(self, screen: pygame.Surface):
        self.draw_head(screen)
        self.draw_body(screen)

    def move(self):
        self.move_body()
        self.move_head()

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((30, 30, 30))

for y in range(0, HEIGHT, 50):
    pygame.draw.line(background, (60, 60, 60), (0, y), (WIDTH, y))
            
snake = Snake(WIDTH, HEIGHT, HEAD_SIZE)
food = Food(30, WIDTH, HEIGHT, HEAD_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    screen.blit(background, (0, 0))
    food.draw(screen)

    if snake.head.colliderect(food.rect):
        snake.grow()
        food.respawn([snake.head, *snake.body])

    snake.draw(screen)
    snake.move()
    snake.change_direction()
    
    pygame.display.update()
    clock.tick(FPS)