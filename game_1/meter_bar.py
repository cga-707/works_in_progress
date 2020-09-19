import pygame

from pygame.sprite import Sprite

class Meter(Sprite):
    """Represents a meter to count remaining bullets"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.meter_color

        self.rect = pygame.Rect(self.settings.meter_x, self.settings.meter_y,
                                self.settings.meter_width, self.settings.meter_height)

    def draw_meter(self):
        """Draw meter"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bars(Sprite):
    """Makes the bars for the meter"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.rect = pygame.Rect(self.settings.meter_x + 2, self.settings.meter_y,
                                self.settings.meter_width - 5, self.settings.bar_height - 5)

    def draw_bar(self):
        """Draw bar"""
        # Change later
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)