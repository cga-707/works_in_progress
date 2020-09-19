class Settings:
    """A class that stores all settings for Alien Invasion"""

    def __init__(self):
        """Intialize the game's static settings"""

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60, 60)

        self.ship_class = 1

        # Default Ship
        if self.ship_class == 1:
            # Ship Class #1
            self.ship_speed = 10.0
            self.bullet_speed = 5.0
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = (0, 235, 30)
            self.bullets_allowed = 6
        # Alien Rebel Ship
        elif self.ship_class == 2:
            # Ship Class #2
            self.ship_speed = 20.0
            self.bullet_speed = 15.0
            self.bullets_allowed = 1
            self.bullet_width = 200
            self.bullet_height = 50
            self.bullet_color = (230, 50, 1)

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 255, 200)
        self.name_game = 'Alien Invasion'
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Meter Setting
        self.meter_color = (100, 100, 100)
        self.meter_width = 61
        self.meter_height = 230
        self.meter_x = 20
        self.meter_y = 650
        # Calculates height of bars
        self.avaliable_barspace = self.meter_height

        self.bar_height = (self.avaliable_barspace) / self.bullets_allowed

        # How quickly the game speeds up
        self.speedup_scale = 1.3

        # How quickly the score scales up
        self.score_scale = 1.5

        self.intialize_dynamic_settings()

    def intialize_dynamic_settings(self):
        """Initialize settings that change throughout a game"""
        # Determines ship class

        self.alien_speed = 5.0

        # fleet_direction; 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

        if self.ship_class == 1:
            self.bullet_speed = 5.0
            self.ship_speed = 10.0
        elif self.ship_class == 2:
            self.ship_speed = 20.0
            self.bullet_speed = 35.0

    def increase_speed(self):
        """Increases speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)






