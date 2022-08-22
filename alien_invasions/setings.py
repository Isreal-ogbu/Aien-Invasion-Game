import pygame.image


class settings:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 700
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor = 6.0
        self.ship_limit = 3
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 0, 60
        self.bullets_allowed = 15
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
