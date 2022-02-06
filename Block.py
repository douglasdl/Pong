import pygame, sys
from config import *

class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pong')

    # Game objects
    block = Block('./images/Paddle.png', 20, SCREEN_HEIGHT/2)
    paddle_group = pygame.sprite.Group()
    paddle_group.add(block)

    while True:
        # Handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()

        # Background Visuals
        screen.fill(BG_COLOR)

        # Drawing the game objects
        paddle_group.draw(screen)

        pygame.display.flip()
        clock.tick(120)