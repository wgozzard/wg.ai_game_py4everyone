

class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Invasion inactive state.
        self.game_active = False
        self.high_score = 0


    def reset_stats(self):
        """Initialize stats that can be reset during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1