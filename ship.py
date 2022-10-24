import pygame

class Ship:
    """ Class to manage the ship """

    def __init__(self,ai_game) -> None:
        """ Initialize the ship """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start the image at middle bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_Right = False
        self.moving_Left = False 

    def blitme(self):
        """ Display the image """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ update the postion based on movement """
        if self.moving_Right:
            self.rect.x += 1

        if self.moving_Left:
            self.rect.x -= 1