import pygame
from display_box import Label
from health_bar import Bar

class Trex(object):
    """Class for the tyrannosaurus rex"""
    def __init__(self, screen, x=50, y=193, width=100, height=10):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load('images/dino_clear_small.png')
        self.image_1 = pygame.image.load('images/dino_clear_small.png')
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health_green = Bar(self.screen)
        self.health_red = Bar(self.screen)
        self.health_x = 120
        self.health_y = 220
        self.hurt = False

    def draw_dino(self, dino = 'dino'):
        """Draws the dinosaur"""
        if self.health_green.health > 0:
            if not self.hurt:
                self.image = self.image_1
                self.screen.blit(self.image, self.rect)
                self.health_red.draw_bar((200,0,0), self.health_x, self.health_y)
                self.health_green.draw_bar((0,200,0), self.health_x, self.health_y)
            else:
                if dino == 'dino':
                    self.image = pygame.image.load('images/dino_clear_small_hurt.png')
                elif dino == 'pt':
                    self.image = pygame.image.load('images/pt_hurt.png')
                self.screen.blit(self.image, self.rect)
                self.health_red.draw_bar((200, 0, 0), self.health_x, self.health_y)
                self.health_green.draw_bar((0, 200, 0), self.health_x, self.health_y)

class Pt(Trex):
    """Class for the pterodactyl"""
    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load('images/pt.png')
        self.image_1 = pygame.image.load('images/pt.png')
        self.x = 660
        self.y = 220
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health_x = 700
        self.health_y = 190
