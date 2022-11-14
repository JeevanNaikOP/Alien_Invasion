class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -11 represents left
        self.fleet_direction =1

        self.ship_limit = 3

        # How quickly game speeds ups
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that changes during game """
        self.bullet_speed = 1.5
        self.ship_speed = 2.5
        self.alien_speed = 1.0

        # fleet direction 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """ Increase speed settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

