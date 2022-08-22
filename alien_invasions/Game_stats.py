class Gamestats:
    def __init__(self, a1_settings):
        self.a1_setings = a1_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.a1_setings.ship_limit
        self.score = 0
