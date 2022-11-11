import pygame.font

class Button:
    """ Class to build button for the game """

    def __init__(self,ai_game,msg):
        """ Initialize button attribute """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()