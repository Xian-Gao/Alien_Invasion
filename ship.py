import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its initial location"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship and get its outline rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Locate each ship at the middle of the screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store float numbers in self.center
        self.center = float(self.rect.centerx)

        # Moving signal
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Change the location of the ship according to the moving signal"""
        # Update center rather than rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect according to center
        self.rect.centerx = self.center

    def blitme(self):
        """Paint ship at the given location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Set the ship middle"""
        self.center = self.screen_rect.centerx