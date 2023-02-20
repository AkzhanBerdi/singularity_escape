import pygame
game_over = False
GRAVITY_FORCE = 5
SPEED = 10

class Sattelite(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/sattelite.png')
        self.rect = self.image.get_rect()
        self.x = -100
        self.y = -100
        self.rect.center = [x,y]
        self.height = 40
        self.width = 40

    def update(self):
        if game_over == False:
            if self.rect.centery + self.height < 280:
                self.rect.centery += GRAVITY_FORCE
            if self.rect.centerx + self.width > 375:
                self.rect.centerx -= GRAVITY_FORCE
            if self.rect.centery + self.height > 280:
                self.rect.centery -= GRAVITY_FORCE
            if self.rect.centerx + self.width < 375:
                self.rect.centerx += GRAVITY_FORCE  
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT] and self.rect.centerx < 675:
                self.rect.centerx += SPEED
            if key[pygame.K_LEFT] and self.rect.centerx > 20:
                self.rect.centerx -= SPEED
            if key[pygame.K_UP] and self.rect.centery > 15:
                self.rect.centery -= SPEED
            if key[pygame.K_DOWN] and self.rect.centery < 685:
                self.rect.centery += SPEED