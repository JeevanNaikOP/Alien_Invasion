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
            self._check_events()

            self.ship.update()

            self._update_screen()

            # make the loop run 60 times per second
            self.clock.tick(60)

    def _check_events(self):
        """ Responds to keypress """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right
                    self.ship.moving_Right = True

                if event.key == pygame.K_LEFT:
                    # move the ship to left
                    self.ship.moving_Left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # stop the movement of ship
                    self.ship.moving_Right = False

                if event.key == pygame.K_LEFT:
                    # stop the movement of ship
                    self.ship.moving_Left = False    

                

    def _update_screen(self):
        """ Update screen"""
        # fill the background
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        
        # make the most recent drawn on screen visible
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
                