import pygame
from display_box import Label

class SelectBox(object):
    def __init__(self, screen):
        self.screen = screen

        self.x1 = 3
        self.y1 = 500
        self.x2 = 500
        self.y2 = 500
        self.x3 = 500
        self.y3 = 595
        self.x4 = 3
        self.y4 = 595

        self.points = [(self.x1, self.y1), (self.x2, self.y2),
                       (self.x3, self.y3), (self.x4, self.y4), (self.x1, self.y1)]

        self.left_side = True
        self.right_side = False
        self.up_pos = True
        self.down_pos = False


    def draw_lines(self):
        """Draws the lines that make up the selection box"""
        pygame.draw.lines(self.screen, (200,200,200), True, self.points, width=10)

    def go_right(self):
        """Makes the selection box go right"""
        if self.left_side:
            self.x1 += 500
            self.x2 += 495
            self.x3 += 495
            self.x4 += 500
            self.left_side = False
            self.right_side = True

            self.points = [(self.x1, self.y1), (self.x2, self.y2),
                           (self.x3, self.y3), (self.x4, self.y4), (self.x1, self.y1)]

    def go_left(self):
        """Makes the selection box go left"""
        if self.right_side:
            self.x1 -= 500
            self.x2 -= 495
            self.x3 -= 495
            self.x4 -= 500
            self.right_side = False
            self.left_side = True

            self.points = [(self.x1, self.y1), (self.x2, self.y2),
                           (self.x3, self.y3), (self.x4, self.y4), (self.x1, self.y1)]

    def go_down(self):
        """Makes the selection box go down"""
        if self.up_pos:
            self.y1 += 100
            self.y2 += 100
            self.y3 += 100
            self.y4 += 100
            self.up_pos = False
            self.down_pos = True

            self.points = [(self.x1, self.y1), (self.x2, self.y2),
                           (self.x3, self.y3), (self.x4, self.y4), (self.x1, self.y1)]

    def go_up(self):
        """Makes the selection box go up"""
        if self.down_pos:
            self.y1 -= 100
            self.y2 -= 100
            self.y3 -= 100
            self.y4 -= 100
            self.down_pos = False
            self.up_pos = True

            self.points = [(self.x1, self.y1), (self.x2, self.y2),
                           (self.x3, self.y3), (self.x4, self.y4), (self.x1, self.y1)]
