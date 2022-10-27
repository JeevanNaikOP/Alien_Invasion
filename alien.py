import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A claa for single alien """

    def __init__(self,ai_game):
        """ Initialize alien and starting position """
        super().__init__()
        self.screen = ai_game.screen

        # load the image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start new alien at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien horizontal poition
        self.x = float(self.rect.x)