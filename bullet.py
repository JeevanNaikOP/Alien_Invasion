import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Sprite will group related item """
    def __init__(self,ai_game):
        # Create a bullet opject at current position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_height,self.settings.bullet_width)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """ Update the bullet position"""
        self.y -= self.settings.bullet_speed

        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw bullet to the screen """
        pygame.draw.rect(self.screen,self.color,self.rect)