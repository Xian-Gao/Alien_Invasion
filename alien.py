import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing single alien"""

    def __init__(self, ai_settings, screen):
        """Initialize alien aand set its initial location"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each alien is at the right of the top initially
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the accurate location of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Paint alien at the given location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if the alien is on the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien left or right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x


