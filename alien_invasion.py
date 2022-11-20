import sys
import pygame
from settings import Settings
from ship import Ship 
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard

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

        # create an instance to store game
        self.stats = GameStats(self)

        # Start Alien Invasion in inactive state
        self.game_active = False

        # make the play button
        self.play_button = Button(self,"Play")

        # Scoreboard instance
        self.sb = Scoreboard(self)

    def run_game(self):
        """ Start the main game """
        while True:
            # checking keyboard and mouse
            self._check_events()

            if self.game_active:

                self.ship.update()

                self._update_alien()

                self.bullets.update()

                self._remove_bullet()

                self._check_collision()

                self._add_fleet()
            
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                

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

        self.sb.show_score()

        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        
        # draw the play button if game is inactive
        if not self.game_active:
            self.play_button.draw_button()

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
        """ update the position of alien """
        self._check_fleet_edge()
        self.aliens.update()

    def _create_alien(self,current_x,current_y):
        """ Create an alien and place it in the row """
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.rect.y = current_y

        self.aliens.add(new_alien)

    def _check_fleet_edge(self):
        """ Check if aliens have reached edge """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                return

    def _change_fleet_direction(self):
        """ drop the fleet and change direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_collision(self):
        """ check for collision of bullet with alien or alien with ship """
        # remove alien if bullet collides with ship
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if collisions:
            # number of alien collided
            for collision in collisions.values():
                self.stats.score += self.settings.alien_points * len(collision)
            self.sb._prep_msg()
            self.sb.check_highscore()

        # if alien collides with ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # check if alien collides with bottom of the screen
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """ Check if you have reached the bottom of screen """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _add_fleet(self):
        """ Destroy existing bullet create new fleet """
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _ship_hit(self):
        """ Respond to the ship hit by alien """
        if self.stats.ships_left >= 0:
            # Decrement ship left
            self.stats.ships_left =- 1

            # Get rid of aliens and bullets
            self.bullets.empty()
            self.aliens.empty()

            # create new fleet
            self._create_fleet()

            # Pause
            sleep(0.5)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_play_button(self,mouse_pos):
        """ Start game when mouse clicks play button """
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            # Reset game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()

            # reset score
            self.sb._prep_msg()

            self.game_active = True

            # Empty bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # create alien fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            # hide mouse cursor
            pygame.mouse.set_visible(False)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
                