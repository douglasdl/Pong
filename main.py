import pygame, sys, random, os
import pygame.freetype

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Limit the ball to the screen
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound) 
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    
    # Collision detection with players
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_animation():
    global player_size
    player.y += player_speed
    # Limit the player to the screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    


def opponent_ai():
    # Opponent AI
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Limit the opponent to the screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
    
    if current_time - score_time < 1000:
        countdown = game_font.render('3', False, WHITE)
        screen.blit(countdown, (screen_width/2 - 10, screen_height/2 - 50))
    if 1000 < current_time - score_time < 2000:
        countdown = game_font.render('2', False, WHITE)
        screen.blit(countdown, (screen_width/2 - 10, screen_height/2 - 50))
    if 2000 < current_time - score_time < 3000:
        countdown = game_font.render('1', False, WHITE)
        screen.blit(countdown, (screen_width/2 - 10, screen_height/2 - 50))

    if current_time - score_time < 3000:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None
    


# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Set up the main window
screen_width = 1000
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
bg_color = pygame.Color('grey12')
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (80, 80, 155)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


# Game Rectangles
player_size = 70
opponent_size = 70
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - player_size, 10, player_size * 2)
opponent = pygame.Rect(10, screen_height/2 - opponent_size, 10, opponent_size * 2)

# Game variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

# Texture variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32) 

# Score Timer
score_time = True

tx = 64
ty = 64

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts", "Jellee-Bold.ttf")
font_size = tx
pygame.freetype.init()
myfont = pygame.freetype.Font(font_path, font_size)

# Sound
pong_sound = pygame.mixer.Sound('pong.ogg')
score_sound = pygame.mixer.Sound('score.ogg')


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
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        
        # DOWN
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


    # Game logic
    ball_animation()
    player_animation()
    opponent_ai()


    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, LIGHT_GREY, player)
    pygame.draw.rect(screen, LIGHT_GREY, opponent)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.aaline(screen, LIGHT_GREY, (screen_width/2, 0), (screen_width/2, screen_height))

    # Display Score
    myfont.render_to(screen, (screen_width/2 - 150, 10), "Opponent: "+str(opponent_score), WHITE, None, size=20)
    myfont.render_to(screen, (screen_width/2 + 20, 10), "Player: "+str(player_score), WHITE, None, size=20)

    if score_time:
        ball_start()

    player_text = game_font.render(str(player_score), True, WHITE)
    screen.blit(player_text, (screen_width/2 + 30, screen_height/2))

    opponent_text = game_font.render(str(opponent_score), True, WHITE)
    screen.blit(opponent_text, (screen_width/2 - 40, screen_height/2))

    # Update the screen
    pygame.display.flip()
    clock.tick(60)