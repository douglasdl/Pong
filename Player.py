import pygame, sys
from config import *
from Block import Block

class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0
        self.size = 70
    
    # Limit the player to the screen
    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    
    def update(self, ball_group = None):
        self.rect.y += self.movement
        self.screen_constrain()


if __name__ == "__main__":
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    middle_strip = pygame.Rect(SCREEN_WIDTH/2 - 2, 0, 4, SCREEN_HEIGHT)

    # Game objects
    player = Player('./images/Paddle.png', SCREEN_WIDTH - 20, SCREEN_HEIGHT/2, 5)
    paddle_group = pygame.sprite.Group()
    paddle_group.add(player)

    while True:
        # Handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()

            # Check if arrow buttons are pressed
            # UP
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.movement += player.speed
                if event.key == pygame.K_UP:
                    player.movement -= player.speed
            
            # DOWN
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player.movement -= player.speed
                if event.key == pygame.K_UP:
                    player.movement += player.speed

        # Background Visuals
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, ACCENT_COLOR, middle_strip)
        
        # Run the game
        # Drawing the game objects
        paddle_group.draw(screen)

        # Updating the game objects
        paddle_group.update()

        # Update the screen rendering
        pygame.display.flip()
        clock.tick(120)