import pygame

class Kirby:
    """A class to manage Kirby """

    def __init__(self, ai_game):
        """Initializes Kirby and sets him on his starting point"""
        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/kirby2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)