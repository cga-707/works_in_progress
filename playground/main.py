# Make enemy dino attack back

import pygame

from display_box import DisplayBox
from display_box import Label
from select_box import SelectBox
from dino import Trex
from dino import Pt
from textures import draw_grass
from dino_sprite import DinoSprite
from attacks import PAttack
from time import sleep


def draw_borders():
    """Draws the borders for the display box"""
    pygame.draw.line(win, (80, 40, 2), (0, 500), (1000, 500), width=10)
    pygame.draw.line(win, (80, 40, 2), (2, 500), (2, 700), width=10)
    pygame.draw.line(win, (80, 40, 2), (0, 598), (1000, 598), width=5)
    pygame.draw.line(win, (80, 40, 2), (995, 500), (995, 700), width=10)
    pygame.draw.line(win, (80, 40, 2), (0, 694), (1000, 694), width=10)
    pygame.draw.line(win, (80, 40, 2), (502, 500), (502, 700), width=5)


def draw_start_screen(win):
    """Draws the start screen"""
    pygame.draw.rect(win, (0, 70, 0), (0, 0, 1000, 700))
    image = pygame.image.load('images/start.png')
    win.blit(image, (300, 300, 10, 10))


def draw_over_world(win):
    """Draws the over world"""
    pygame.draw.rect(win, (100, 100, 255), (0, 0, 1000, 700))
    area = pygame.image.load('images/area_1x.png')
    win.blit(area, (-5, 0, 10, 10))
    intro = pygame.image.load('images/overworld_text_1.png')
    win.blit(intro, (400, 550, 10, 10))



def redraw_window(display_now, win, overworld, dino_sprite, o_turn):
    """Redraws the game window"""
    if not overworld and not start:
        win.fill((190, 190, 255))
        display_box.draw_box()

    if display_now < 1:
        labels.draw_label('run', 3)
        labels.draw_label('attack', 1)
        labels.draw_label('items', 2)
        labels.draw_label('switch', 4)
    elif display_now == 1:
        enter(attack)


    draw_borders()

    select_box.draw_lines()
    dino.draw_dino('dino')
    pt.draw_dino('pt')
    if fireball.visible:
        fireball.draw_pattack()
        fireball.move_pattack(600, pt)
    if windslice.visible and not fireball.visible:
        windslice.draw_pattack()
        windslice.move_pattack(150, dino, '-')

# Draws the grass
    i = 0
    x = 0
    while i < 10:
        draw_grass(win, x)
        x += 100
        i += 1

# if statement for the overworld
    if overworld:
        draw_over_world(win)
        sleep(0.04)
        dino_sprite.draw_sprite()
        dino_sprite.moving = False
    if start:
        draw_start_screen(win)

    pygame.display.update()


# Initialization for pygame
# and for the different instances
pygame.init()

win = pygame.display.set_mode((1000,700))

pygame.display.set_caption("Playground")

display_box = DisplayBox(win)
labels = Label(win)
select_box = SelectBox(win)


dino = Trex(win)
pt = Pt(win)
fireball = PAttack(win, 'fireball')
windslice = PAttack(win, 'windslice', 500, 220)
dino_sprite = DinoSprite(30, 300, 100, 100, win, False)
display_now = 0
pause = bool()
o_turn = False

def enter(attack):
    """Reacts to the enter key being pressed"""
    attacks = Label(win)
    # Attacks
    if attack == True:
        attacks.draw_label('charge', 3)
        attacks.draw_label('fireball', 1)
        attacks.draw_label('roar', 2)
        attacks.draw_label('scratch', 4)

# Bools for different layers
start = True
overworld = False

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Keyup events
#

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if pause:
                    if start == False and overworld == False:
                        if display_now == 1:
                            if select_box.x1 == 3 and select_box.y1 == 500:
                                fireball.visible = True
                                windslice.visible = True
                            else:
                                None
                                #attack here
                            display_now = 0
                        else:
                            display_now += 1
                            if select_box.x1 == 3 and select_box.y1 == 500:
                                attack = True
                            elif select_box.x1 == 503 and select_box.y1 == 600:
                                overworld = True
                                attack = False
                                dino.health_green.lose_health(int(dino.health_red.health * 0.15))
                                display_now -= 1
                            else:
                                attack = False
                    if start:
                        start = False
                        overworld = True
            elif event.key == pygame.K_BACKSPACE:
                if not overworld and not start:
                    display_now -= 1
            elif event.key == pygame.K_DOWN:
                if overworld:
                    overworld = False


# Key press events
#
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        run = False
    if keys[pygame.K_RIGHT]:
        if dino_sprite.x < 70:
            dino_sprite.moving = True
            dino_sprite.x += dino_sprite.vel
        if not overworld and not start:
            select_box.go_right()
    elif keys[pygame.K_LEFT]:
        if dino_sprite.x > 10:
            dino_sprite.moving = True
            dino_sprite.x -= dino_sprite.vel
        if not overworld and not start:
            select_box.go_left()
    elif keys[pygame.K_DOWN]:
        if not overworld and not start:
            select_box.go_down()
    elif keys[pygame.K_UP]:
        if not overworld and not start:
            select_box.go_up()

# redraws game window
    redraw_window(display_now, win, overworld, dino_sprite, o_turn)


# List of actions that pause game while taking place
    if not fireball.visible:
        pause = True
    else:
        pause = False




pygame.quit()


