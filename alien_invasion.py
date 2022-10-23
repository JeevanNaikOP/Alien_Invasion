import sys
import pygame

class AlienInvasion:
    def __init__(self):
        """ initialize pygame """
        pygame.init()

        pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien invasion")

        self.clock = pygame.time.Clock()

        # set background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """ Start the main game """
        while True:
            # checking keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()

            # fill the background
            self.screen.fill(self.bg_color)
            # make the most recent drawn on screen visible
            pygame.display.flip()

            # make the loop run 60 times per second
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
                