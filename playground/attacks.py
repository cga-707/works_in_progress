import pygame

from damage_settings import damage_rand
from time import sleep

class PAttack(object):
    """Draws a basic attack"""
    def __init__(self, screen, name, x=180, y=250):
        self.name = name
        self.screen = screen
        self.image = pygame.image.load(f'images/{self.name}_attack.png')
        self.x = x
        self.y = y
        self.xx = x
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.visible = False
        self.clear = (0, 0, 0, 0)

    def draw_pattack(self):
        """Draws an attack"""
        if self.visible:
            self.screen.blit(self.image, self.rect)

    def move_pattack(self, end, char, dir = '+'):
        """Moves the attack across the screen"""
        if dir == '+':
# This is for the attack animation of the ally dinosaur
            if self.x < end:
                self.image = pygame.image.load(f'images/{self.name}_attack.png')
                self.x += 10
                self.rect = pygame.Rect(self.x, self.y, 100, 100)

                # This makes the dinosaur turn gray at the right frame
                if self.x == end - 10:
                    char.hurt = True
            else:
                # Make the attack invisible
                self.visible = False
                damage = damage_rand(20, 30)
                char.health_green.lose_health(damage)
                self.image.fill(self.clear)
                self.x = 180
                self.visible = False
                sleep(0.5)
                char.hurt = False
# This is the animation of the enemy dino
        elif dir == '-':
            if self.x > end:
                if self.x == self.xx:
                    print('pt uses ws')
                    sleep(0.9)
                self.image = pygame.image.load(f'images/{self.name}_attack.png')
                self.x -= 10
                self.rect = pygame.Rect(self.x, self.y, 100, 100)
                # This makes the dinosaur turn gray at the right frame
                if self.x == end + 10:
                    char.hurt = True
            else:
                # Make the attack invisible
                damage = damage_rand(20, 30)
                char.health_green.lose_health(damage)
                self.image.fill(self.clear)
                self.x = self.xx
                if char.hurt:
                    sleep(0.5)
                self.visible = False
                sleep(0.5)
                char.hurt = False







