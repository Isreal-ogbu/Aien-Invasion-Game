import pygame


class Ship:
    def __init__(self, a1_settings, screen):
        self.screen = screen
        self.a1_settings = a1_settings
        # load screen image and get it erect
        self.image = pygame.image.load('Image/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.a1_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.a1_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        # To draw the ship at the centre
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
