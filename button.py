import pygame
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
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