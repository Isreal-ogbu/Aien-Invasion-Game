import pygame
from pygame.sprite import  Sprite


class Alien(Sprite):
    def __init__(self, a1_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.a1_settings = a1_settings

        # load the alien image from the Image folder
        self.image = pygame.image.load('Image/alien11.bmp')
        self.rect = self.image.get_rect()

        # Start new alien image from the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store th alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.a1_settings.alien_speed_factor * self.a1_settings.fleet_direction)
        self.rect.x = self.x