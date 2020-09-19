import pygame

class Bar(object):
    """Models a Bar"""
    def __init__(self, screen):
        self.screen = screen

        self.health = 100
        self.height = 10



    def draw_bar(self, color, x, y):
        """Draws the health bar"""
        rect = pygame.Rect(x, y, self.health, self.height)
        pygame.draw.rect(self.screen, color, rect)

    def lose_health(self, damage):
        if self.health > 0:
            self.health -= damage


