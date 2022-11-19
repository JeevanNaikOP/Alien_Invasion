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

        # score image
        self._prep_msg()

    def _prep_msg(self):
        """ Turn score into rendered image  """
        score_val = str(self.stats.score)

        self.score_img = self.font.render(score_val,True,self.text_color,self.settings.bg_color)
        
        # Display imag at top right of the screen
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def show_score(self):
        """ Display score on the screen """
        self.screen.blit(self.score_img,self.score_img_rect)
