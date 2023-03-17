import pygame
from pygame.locals import *
import pygame.mixer
import random
from meteor import Meteor
from hole import Hole
from sattelite import Sattelite
from button import Button

pygame.init()
clock = pygame.time.Clock()

#CONSTANTS
WIDTH = 700
HEIGHT = 700
FPS = 60

#Music and sound settings
pygame.mixer.music.load('sound/dread.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
sndPoint = pygame.mixer.Sound('sound/point.mp3')
sndPoint.set_volume(0.13)

# image file path
space_bg = pygame.image.load('img/space.png')
button_img = pygame.image.load('img/restart.png')

# screen settings
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Singularity Escape")

#Font
font = pygame.font.SysFont('Bauhaus 93',60)

#Colour
white = (255,255,255)

#game_variables
meteor_frequency = 2000
last_meteor = pygame.time.get_ticks() - meteor_frequency
game_over = False
score = 0
evasion = False

#fx
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

def reset_game():
    meteorit_group.empty()
    voyager.rect.centerx = 0
    voyager.rect.centery = 700
    score = 0
    return score

#class objects
black_hole = Hole(360,260)
voyager = Sattelite(600,600)
button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)

# object groups
satel_group = pygame.sprite.Group()
hole_group = pygame.sprite.Group()
satel_group.add(voyager)
hole_group.add(black_hole)
meteorit_group = pygame.sprite.Group()

run = True
while run:
    clock.tick(FPS)
    screen.blit(space_bg, (0,0))
    meteorit_group.draw(screen)
    if game_over == False:
        voyager.update()
        satel_group.update()
    hole_group.draw(screen)
    satel_group.draw(screen)
    hole_group.update()
    screen.blit(voyager.image,(voyager.x,voyager.y))

    #checking_score
    if len(meteorit_group) > 0:
        if satel_group.sprites()[0].rect.left != meteorit_group.sprites()[0].rect.left\
            and satel_group.sprites()[0].rect.right != meteorit_group.sprites()[0].rect.right\
            and evasion == False:
            evasion = True
        if evasion == True and game_over == False:
            if satel_group.sprites()[0].rect.left != meteorit_group.sprites()[0].rect.right:
                score += 1
                evasion = False
            if score in {100,200,300,400,500,600,700,800,900,1000}:
                sndPoint.play(0)
                meteor_frequency -= 180

    draw_text(str(score),font,white,int(WIDTH/2),20)

    #collide_event
    if pygame.sprite.groupcollide(satel_group,meteorit_group,False,False):
        game_over = True
        button.draw()

    if pygame.sprite.groupcollide(satel_group,hole_group,False,False):
        game_over = True
        button.draw()

    if game_over == False:

        time_now = pygame.time.get_ticks()

        if time_now - last_meteor > meteor_frequency:
            left_meteor = Meteor(0,random.randint(0,690))
            bottom_meteor = Meteor(random.randint(0,690),690)
            right_meteor = Meteor(690,random.randint(0,690))
            top_meteor = Meteor(random.randint(0,690),0)
            meteorit_group.add(left_meteor)
            meteorit_group.add(bottom_meteor)
            meteorit_group.add(right_meteor)
            meteorit_group.add(top_meteor)
            last_meteor = time_now
        meteorit_group.update()

    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()
            meteor_frequency = 2000

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
            run = False

    pygame.display.update()
pygame.quit()