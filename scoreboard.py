import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """ A class to report scoring information """

    def __init__(self,ai_game):
        """ Initialize scoring attribute """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # score image
        self._prep_msg()

        # score high score
        self.prep_high_score()

        # dispaly level
        self.prep_level()

        # display number of ship
        self.prep_ships()

    def _prep_msg(self):
        """ Turn score into rendered image  """
        rounded_score = round(self.stats.score,-1)

        score_val = f"{rounded_score:,}"

        self.score_img = self.font.render(score_val,True,self.text_color,self.settings.bg_color)
        
        # Display imag at top right of the screen
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def show_score(self):
        """ Display score on the screen """
        self.screen.blit(self.score_img,self.score_img_rect)
        self.screen.blit(self.high_score_img,self.high_score_img_rect)
        self.screen.blit(self.level_img,self.level_img_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """ Turn the highscore into rendered image """
        high_score = round(self.stats.score,-1)

        high_score_val = f"{high_score:,}"

        self.high_score_img = self.font.render(high_score_val,True,self.text_color,self.settings.bg_color)
        
        # Display imag at top right of the screen
        self.high_score_img_rect = self.high_score_img.get_rect()
        self.high_score_img_rect.right = self.screen_rect.centerx
        self.high_score_img_rect.top = 20

    def check_highscore(self):
        """ Check to see if there is new highscore """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """ Turn the level into rendered image """
        level_str = str(self.stats.level)

        self.level_img = self.font.render(level_str,True,self.text_color,self.settings.bg_color)
        
        # Display imag at top right of the screen
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.right = self.score_img_rect.right
        self.level_img_rect.top = self.score_img_rect.bottom + 10

    def prep_ships(self):
        """ Turn the level into rendered image """
        self.ships = Group()

        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    