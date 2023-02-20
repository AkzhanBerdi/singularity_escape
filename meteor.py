import pygame
from pygame.locals import *
import pygame.mixer
GRAVITY_FORCE = 5

class Meteor(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/meteorit.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    
    def update(self):
        if self.rect.centerx > 350:
            self.rect.centerx -= GRAVITY_FORCE
        if self.rect.centerx < 350:
            self.rect.centerx += GRAVITY_FORCE
        if self.rect.centery < 250:
            self.rect.centery += GRAVITY_FORCE
        if self.rect.centery > 250:
            self.rect.centery -= GRAVITY_FORCE
        if self.rect.centerx == 300 and self.rect.centery >= 230:
            self.kill()
        if self.rect.centerx == 370 and self.rect.centery <= 330:
            self.kill()
        if self.rect.centerx == 300 and self.rect.centery <= 330:
            self.kill()
        if self.rect.centerx == 370 and self.rect.centery >= 230:
            self.kill()
        if self.rect.centerx >= 300 and self.rect.centery == 230:
            self.kill()
        if self.rect.centerx <= 370 and self.rect.centery == 330:
            self.kill()
        if self.rect.centerx >= 300 and self.rect.centery == 330:
            self.kill()
        if self.rect.centerx <= 370 and self.rect.centery == 230:
            self.kill()