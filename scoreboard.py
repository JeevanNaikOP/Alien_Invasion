import pygame.font

class Scoreboard:
    """ A class to report scoring information """

    def __init__(self,ai_game):
        """ Initialize scoring attribute """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
