import pygame
from pygame.locals import *
import pygame.mixer
import random

pygame.init()
clock = pygame.time.Clock()

#CONSTANTS
WIDTH = 700
HEIGHT = 700
SPEED = 10
GRAVITY_FORCE = 5
FPS = 60

#Music and sound settings
pygame.mixer.music.load('dread.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
sndPoint = pygame.mixer.Sound('point.mp3')
sndPoint.set_volume(0.13)

# image file path
hole_image = pygame.image.load('hole1.png')
space_bg = pygame.image.load('space.png')
button_img = pygame.image.load('restart.png')

# screen settings
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dino Game")

#Font
font = pygame.font.SysFont('Bauhaus 93',60)

#Colour
white = (255,255,255)

#game_variables
meteor_frequency = 1500
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
    DINO.rect.x = 500
    DINO.rect.y = 700
    score = 0
    return score

#classes
class Meteor(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('meteorit.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    """#position from all sides
        if position == 1:
            self.rect.bottomleft = [x,y]
        if position == 2:
            self.rect.bottom = [x,y]
        if position == 3:
            self.rect.bottom = [x,y]
        if position == 4:
            self.rect.bottom = [x,y]"""
    
    def update(self):
        if self.rect.x > 350:
            self.rect.x -= GRAVITY_FORCE
        if self.rect.x < 350:
            self.rect.x += GRAVITY_FORCE
        if self.rect.y < 250:
            self.rect.y += GRAVITY_FORCE
        if self.rect.y > 250:
            self.rect.y -= GRAVITY_FORCE
        if self.rect.x == 350 and self.rect.y == 250:
            self.kill()
        

class Hole(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hole1.png')
        self.rect = self.image.get_rect()
        #unneccessary?
        self.rect.center = [x, y]
        

class Sattelite(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sattelite.png')
        #self.index = 0
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.x_axis = 600
        self.y_axis = 400
        self.height = 40
        self.width = 40

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            action = True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

#class objects
black_hole = Hole(360,260)
DINO = Sattelite(700,500)
button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)

# object groups
satel_group = pygame.sprite.Group()
hole_group = pygame.sprite.Group()
satel_group.add(DINO)
hole_group.add(black_hole)
meteorit_group = pygame.sprite.Group()

run = True
while run:
    clock.tick(FPS)
    screen.blit(space_bg, (0,0))
    meteorit_group.draw(screen)
    satel_group.update()
    screen.blit(hole_image,(270,170))
    screen.blit(DINO.image,(DINO.x_axis,DINO.y_axis))

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
            if score in {1000,2000,3000,4000,5000,6000,7000,8000,9000}:
                sndPoint.play(0)
    draw_text(str(score),font,white,int(WIDTH/2),20)

    #collide_event
    if pygame.sprite.spritecollide(DINO,meteorit_group,False,False):
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

        #keys = pygame.key.get_pressed()
        if DINO.y_axis + DINO.height < 300:
            DINO.y_axis += GRAVITY_FORCE
        if DINO.x_axis + DINO.width > 400:
            DINO.x_axis -= GRAVITY_FORCE
        if DINO.y_axis + DINO.height > 300:
            DINO.y_axis -= GRAVITY_FORCE
        if DINO.x_axis + DINO.width < 400:
            DINO.x_axis += GRAVITY_FORCE  

        # Key_press actions
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and DINO.x_axis < 665:
            DINO.x_axis += SPEED
        if key[pygame.K_LEFT] and DINO.x_axis > 5:
            DINO.x_axis -= SPEED
        if key[pygame.K_UP] and DINO.y_axis > 15:
            DINO.y_axis -= SPEED
        if key[pygame.K_DOWN] and DINO.y_axis < 660:
            DINO.y_axis += SPEED
        if key[pygame.K_SPACE]:
            DINO.y_axis += 45
            DINO.y_axis -= 40

    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
            run = False

    pygame.display.update()
pygame.quit()