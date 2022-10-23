import sys
import pygame
from settings import Settings
from ship import Ship 

class AlienInvasion:
    def __init__(self):
        """ initialize pygame """
        pygame.init()

        self.clock = pygame.time.Clock()

        # set background color and window
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)

    def run_game(self):
        """ Start the main game """
        while True:
            # checking keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # fill the background
            self.screen.fill(self.settings.bg_color)

            self.ship.blitme()

            # make the most recent drawn on screen visible
            pygame.display.flip()

            # make the loop run 60 times per second
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
                