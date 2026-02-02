class Gamestats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        # High score should never be reset.
        self.high_score = 0
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Load the high score from a file
        self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from a file."""
        try:
            with open(self.ai_settings.high_score_file) as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0