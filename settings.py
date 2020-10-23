class Settings():
    """A class that stores all the settings in Alien Invasion"""

    def __init__(self):
        """Initialize the static settings of game"""
        # Settings of screen
        self.screen_width = 1200
        self.screen_height = 675
        self.bg_color = (230, 230, 230)

        # settings of ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Settings of bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Settings of aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # Accelerate the game in what speed
        self.speedup_scale = 1.1

        # Speed of alien score increasing
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize the settings that change with the game process"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet direction = 1 means moving right, -i means left
        self.fleet_direction = 1

        # Record score
        self.alien_points = 50


    def increase_speed(self):
        """Setting to increase speed and alien score"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)