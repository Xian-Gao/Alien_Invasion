import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the bullets that the ship shoots"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's location"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a rectangle representing bullet at (0,0) and set the correct location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's location in float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet on"""
        # Update the float representing bullet
        self.y -= self.speed_factor

        # Update rect representing bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """Paint bullets on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
