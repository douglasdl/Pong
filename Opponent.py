import pygame, sys
from config import *
from Block import Block

class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.size = 70
    
    def update(self, ball_group = None):
        if ball_group != None:
            if self.rect.top < ball_group.sprite.rect.y:
                self.rect.y += self.speed
            if self.rect.bottom > ball_group.sprite.rect.y:
                self.rect.y -= self.speed
            self.constrain()
        else:
            # Move Up until reach the top then move down until reach the bottom
            self.rect.y -= self.speed
            if self.rect.top <= 0:
                self.speed *= -1
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.speed *= -1
            self.constrain()


    def constrain(self):
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT


if __name__ == '__main__':
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    middle_strip = pygame.Rect(SCREEN_WIDTH/2 - 2, 0, 4, SCREEN_HEIGHT)

    # Game objects
    opponent = Opponent('./images/Paddle.png', 20, SCREEN_HEIGHT/2, 5)
    paddle_group = pygame.sprite.Group()
    paddle_group.add(opponent)

    while True:
        # Handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()

        # Background Visuals
        screen.fill(BG_COLOR)

        # Updating the game objects
        opponent.update()

        # Drawing the game objects
        paddle_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)