class GameStats:
    """ Tracking statistics of ship """

    def __init__(self, ai_game) -> None:
        """ Initialize statistics """
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Iitialize statistics during the game """
        self.ships_left = self.settings.ship_limit