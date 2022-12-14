class GameStats:
    """ Tracking statistics of ship """

    def __init__(self, ai_game) -> None:
        """ Initialize statistics """
        self.settings = ai_game.settings
        self.reset_stats()

        # Highscore
        self.high_score = 0

    def reset_stats(self):
        """ Initialize statistics during the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level =1