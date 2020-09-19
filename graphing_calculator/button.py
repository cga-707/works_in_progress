import pygame

class Button(object):
    """Buttons on the calculator"""
    def __init__(self, screen, msg, x, y, font_size=80):
        self.font_size = font_size
        self.screen = screen
        self.msg = msg
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, self.font_size)
        self.render_item = self.font.render(self.msg, True, (0, 0, 200))

    def draw_button(self):
        """Draws the button"""
        if len(self.msg) < 10:
            self.render_item = self.font.render(self.msg, True, (0, 0, 200))
        else:
            self.msg = self.msg[0: -1]
            self.render_item = self.font.render(self.msg, True, (0, 0, 200))
        self.screen.blit(self.render_item, (self.x, self.y))

class BackDrop(object):
    """The back drop for the buttons"""
    def __init__(self, screen, x, y, width=50, height=50):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.color = (255, 255, 255)

    def draw_back_drop(self):
        """Draws the back drop"""
        pygame.draw.rect(self.screen, self.color, self.rect)