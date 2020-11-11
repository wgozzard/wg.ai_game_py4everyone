class Settings():
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        #default is 3
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 3
        #Bullet_width default is 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 200
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed_factor = 1
        #drop factor default is 10
        self.fleet_drop_speed = 10
        #Speeds up the game
        self.speedup_scale = 1.1
        #How quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        #fleet_direction of 1 represents the right; -1 represents the left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Initialize setting that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
