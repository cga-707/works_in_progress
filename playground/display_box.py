import pygame

class DisplayBox(object):
    def __init__(self, screen):
        self.screen = screen

        self.display_width = 1000
        self.display_height = 200
        self.x = 0
        self.y = 500
        self.rect = pygame.Rect(self.x, self.y, self.display_width,
                                self.display_height)

    def draw_box(self):
        """Draws the box"""
        pygame.draw.rect(self.screen, (0,106,0), self.rect)

class Label(object):
    """This class makes the labels that go in the different selection boxes"""
    def __init__(self, screen):
        self.screen = screen
        self.rect = (10,10,10,10)

    def draw_label(self, keyword, quad):
        """Draws a specfic keyword in one of the four spaces"""
        self.image = pygame.image.load(f"images/{keyword}.png")
        self.quad = quad

# The quadrants of the selection box
        if quad == 1:
            self.rect = pygame.Rect(8, 506, 10, 10)
        elif quad == 2:
            self.rect = pygame.Rect(505, 506, 10, 10)
        elif quad == 3:
            self.rect = pygame.Rect(505, 600, 10, 10)
        elif quad == 4:
            self.rect = pygame.Rect(8, 600, 10, 10)

        self.screen.blit(self.image, self.rect)