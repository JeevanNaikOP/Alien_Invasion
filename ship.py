import pygame
from settings import Settings

class Ship:
    """ Class to manage the ship """

    def __init__(self,ai_game) -> None:
        """ Initialize the ship """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the ship image and its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start the image at middle bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_Right = False
        self.moving_Left = False 

        # store the current horizontal position of ship
        self.x = float(self.rect.x)

    def blitme(self):
        """ Display the image """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ update the postion based on movement """
        if self.moving_Right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_Left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update movement object of ship
        self.rect.x = self.x

    def center_ship(self):
        """ Center ship when called """
        self.rect.midbottom = self.screen_rect.midbottom