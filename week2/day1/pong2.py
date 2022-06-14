

# activity:
# change colors, change background, add sounds

import pygame, sys, random

# bg = pygame.image.load("game.jpg")

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('game.jpg', [0,0])


#REST OF ITEMS ARE BLIT'D TO SCREEN.

pygame.init()

clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PONG")

## Functions

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
     ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
     ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1 

def player_animation():
    
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():

    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)

    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def sound1():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)

#########
    if opponent.top <= 0: opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height -10

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# colors

bg_color = (0,68,129)

light_grey = (255,164,0)

# animation

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice ((1, -1))

player_speed = 0
opponent_speed = 7

#------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()
    sound1()

    screen.fill(bg_color)

    pygame.draw.rect(screen, light_grey, player)

    pygame.draw.rect(screen, light_grey, opponent)

    pygame.draw.ellipse(screen, light_grey, ball)

    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))   

    pygame.display.flip()
    clock.tick(60)

    ##

