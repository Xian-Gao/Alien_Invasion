class GameSatas():
    """Trace statistics"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game is inactive if just started
        self.game_active = False

        # Do not reset the highest score
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that may change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1