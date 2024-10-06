import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

bg_color = (200, 90, 122)
paddle_color = (255,222,173)

class Paddle:
    def __init__(self):
        self.x = 400
        self.y = 600 - 70
        self.width = 120
        self.height = 10
        self.direction = 0
    
    def draw(self):
        pygame.draw.rect(screen, paddle_color, (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height), 0, 2)

    def update(self, direction):
        self.direction = direction
    
    def move(self):
        self.x += self.direction


paddle = Paddle()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                paddle.update(-1)
            elif event.key == pygame.K_RIGHT:
                paddle.update(1)
        elif event.type == pygame.KEYUP:
            paddle.update(0)
        


    screen.fill(bg_color)
    paddle.move()
    paddle.draw()

    pygame.display.flip()


pygame.quit()