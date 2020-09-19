import pygame

def draw_grass(screen, x_pos = 0):
    """Draws in-game grass"""
    grass_image = pygame.image.load('images/grass.png')
    grass_rect = pygame.Rect(x_pos, 355, 10, 10)

    screen.blit(grass_image, grass_rect)
