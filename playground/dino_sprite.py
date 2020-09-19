import pygame

class DinoSprite(object):
    def __init__(self, x, y, width, height, screen, moving):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
# For the moving sprites
        self.moving_sprites = [pygame.image.load('images/dino_sprite_1x.png'),
                       pygame.image.load('images/dino_sprite_2x.png')]
# The sprite that is used when not moving
        self.still_sprite = pygame.image.load('images/dino_sprite_0x.png')
# Bools for if the a leg is either up or down
        self.left_leg = True
        self.right_leg = False

        self.moving = moving
        self.vel = 7

    def draw_sprite(self):
        """Draws the dino sprites"""
        if self.moving:
            if self.left_leg:
                self.screen.blit(self.moving_sprites[0], (self.x, self.y, 10, 10))
                self.left_leg = False
                self.right_leg = True
            elif self.right_leg:
                self.screen.blit(self.moving_sprites[1], (self.x, self.y, 10, 10))
                self.right_leg = False
                self.left_leg = True
        else:
            self.screen.blit(self.still_sprite, (self.x, self.y))

