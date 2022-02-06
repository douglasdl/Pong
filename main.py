import pygame, sys

from config import *
from Player import Player
from Ball import Ball
from Opponent import Opponent
from GameManager import GameManager
    
# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Sounds
pong_sound = pygame.mixer.Sound('./sounds/pong.ogg')
score_sound = pygame.mixer.Sound('./sounds/score.ogg')

middle_strip = pygame.Rect(SCREEN_WIDTH/2 - 2, 0, 4, SCREEN_HEIGHT)

# Game objects
player = Player('./images/Paddle.png', SCREEN_WIDTH - 20, SCREEN_HEIGHT/2, 5)
opponent = Opponent('./images/Paddle.png', 20, SCREEN_HEIGHT/2, 1)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('./images/Ball.png', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 4, 4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite, paddle_group)

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

    # Display Score
    #myfont.render_to(screen, (SCREEN_WIDTH/2 - 150, 10), "Opponent: "+str(opponent_score), WHITE, None, size=20)
    #myfont.render_to(screen, (SCREEN_WIDTH/2 + 20, 10), "Player: "+str(player_score), WHITE, None, size=20)

    
    # Run the game
    game_manager.run_game()

    # Update the screen rendering
    pygame.display.flip()
    clock.tick(120)