import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting point"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        if self.settings.ship_class == 1:
            self.image = pygame.image.load('images/ship2.bmp')
        elif self.settings.ship_class == 2:
            self.image = pygame.image.load('images/alien.bmp')

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Stores a decimal value for this ship's position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the Ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center a new ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)




