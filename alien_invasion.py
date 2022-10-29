import sys
import pygame
from settings import Settings
from ship import Ship 
from bullet import Bullet
from alien import Alien

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

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """ Start the main game """
        while True:
            # checking keyboard and mouse
            self._check_events()

            self.ship.update()

            self._update_alien()

            self.bullets.update()

            self._remove_bullet()

            self._update_screen()

            # make the loop run 60 times per second
            self.clock.tick(60)

    def _check_events(self):
        """ Responds to keypress """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_events_KEYDOWN(event)

            elif event.type == pygame.KEYUP:
                self._check_events_KEYUP(event)
                

    def _check_events_KEYDOWN(self,event):
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_Right = True

        if event.key == pygame.K_LEFT:
            # move the ship to left
            self.ship.moving_Left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            # fire bullet
            self._fire_bullet()

    def _check_events_KEYUP(self,event):
        if event.key == pygame.K_RIGHT:
            # stop the movement of ship
            self.ship.moving_Right = False

        if event.key == pygame.K_LEFT:
            # stop the movement of ship
            self.ship.moving_Left = False

    def _fire_bullet(self):
        """ Create new bullet and add it to new bullet group """
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _remove_bullet(self):
        """ removing bullet from list """
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """ Update screen"""
        # fill the background
        self.screen.fill(self.settings.bg_color)

        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        
        # make the most recent drawn on screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """ Create fleet of alien """
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        
        current_x = alien_width
        current_y = alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width ):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            
            current_y += 2 * alien_height

            # reset current_x to start from left
            current_x = alien_width

    def _update_alien(self):
        """ update the position of """
        self.aliens.update()

    def _create_alien(self,current_x,current_y):
        """ Create an alien and place it in the row """
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.rect.y = current_y

        self.aliens.add(new_alien)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
                