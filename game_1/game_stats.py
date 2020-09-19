import json

class GameStats:
    """Track statistics for ALien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Opens json file to load in universal igh score
        filename = "high_score.json"
        with open(filename) as f:
            self.uni_high_score = json.load(f)

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = self.uni_high_score


    def reset_stats(self):
        """Initialize statistics that can change during a game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

