import pygame

from button import Button, BackDrop
from settings import num_button_x_coor, num_button_y_coor, \
    num_backdrop_x_coor, num_backdrop_y_coor, operators, oper_x_coor, \
    oper_y_coor, oper_bd_x, oper_bd_y

pygame.init()
win = pygame.display.set_mode((500, 500))

def add(num_1, num_2):
    return float(num_1 + num_2)

def subtract(num_1, num_2):
    return float(num_1 - num_2)

def multiple(num_1, num_2):
    return float(num_1 * num_2)

def divide(num_1, num_2):
    return float(num_1 / num_2)

run = True

# Instances and variables
single_press = True
button_num = list()
button_backdrop = list()
operator_list = list()
operator_bd = list()

plus = False
minus = False
mult = False
div = False

nums = list()

for char in operators:
    operator_list.append(Button(win, char, oper_x_coor[char], oper_y_coor[char], 100))
    operator_bd.append(BackDrop(win, oper_bd_x[char], oper_bd_y[char]))

display = Button(win, '', 10, 10)

# Button and Backdrop for numbers 0-9
for num in range(0, 10):
    num_word = str(num)
    button_num.append(Button(win, num_word, num_button_x_coor[num], num_button_y_coor[num]))
    button_backdrop.append(BackDrop(win, num_backdrop_x_coor[num], num_backdrop_y_coor[num]))

# main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if single_press == True:
                single_press = False

                var = pygame.mouse.get_pos()
                if button_backdrop[0].rect.collidepoint(var):
                    display.msg += '0'
                    button_backdrop[0].color = (100, 100, 100)

                elif button_backdrop[1].rect.collidepoint(var):
                    button_backdrop[1].color = (100, 100, 100)
                    display.msg += '1'

                elif button_backdrop[2].rect.collidepoint(var):
                    button_backdrop[2].color = (100, 100, 100)
                    display.msg += '2'

                elif button_backdrop[3].rect.collidepoint(var):
                    button_backdrop[3].color = (100, 100, 100)
                    display.msg += '3'

                elif button_backdrop[4].rect.collidepoint(var):
                    button_backdrop[4].color = (100, 100, 100)
                    display.msg += '4'

                elif button_backdrop[5].rect.collidepoint(var):
                    button_backdrop[5].color = (100, 100, 100)
                    display.msg += '5'

                elif button_backdrop[6].rect.collidepoint(var):
                    button_backdrop[6].color = (100, 100, 100)
                    display.msg += '6'

                elif button_backdrop[7].rect.collidepoint(var):
                    button_backdrop[7].color = (100, 100, 100)
                    display.msg += '7'

                elif button_backdrop[8].rect.collidepoint(var):
                    button_backdrop[8].color = (100, 100, 100)
                    display.msg += '8'

                elif button_backdrop[9].rect.collidepoint(var):
                    button_backdrop[9].color = (100, 100, 100)
                    display.msg += '9'

                elif operator_bd[0].rect.collidepoint(var):
                    operator_bd[0].color = (100, 100, 100)

                    plus = True
                    minus = False
                    mult = False
                    div = False

                    if display.msg != '':
                        nums.append(float(display.msg))
                        display.msg = ''

                elif operator_bd[1].rect.collidepoint(var):
                    operator_bd[1].color = (100, 100, 100)

                    plus = False
                    minus = True
                    mult = False
                    div = False

                    if display.msg != '':
                        nums.append(float(display.msg))
                        display.msg = ''

                elif operator_bd[2].rect.collidepoint(var):
                    operator_bd[2].color = (100, 100, 100)

                    plus = False
                    minus = False
                    mult = True
                    div = False

                    if display.msg != '':
                        nums.append(float(display.msg))
                        display.msg = ''

                elif operator_bd[3].rect.collidepoint(var):
                    operator_bd[3].color = (100, 100, 100)

                    plus = False
                    minus = False
                    mult = False
                    div = True

                    if display.msg != '':
                        nums.append(float(display.msg))
                        display.msg = ''

                elif operator_bd[4].rect.collidepoint(var):
                    operator_bd[4].color = (100, 100, 100)

                    if display.msg != '':
                        nums.append(float(display.msg))
                        display.msg = ''

                        if plus:
                            result = add(nums[0], nums[1])
                            display.msg = str(result)
                            nums.clear()
                        elif minus:
                            result = subtract(nums[0], nums[1])
                            display.msg = str(result)
                            nums.clear()
                        elif mult:
                            result = multiple(nums[0], nums[1])
                            display.msg = str(result)
                            nums.clear()
                        elif div:
                            result = divide(nums[0], nums[1])
                            display.msg = str(result)
                            nums.clear()

        elif event.type == pygame.MOUSEBUTTONUP:
            single_press = True
            for num in range(0, 10):
                button_backdrop[num].color = (255, 255, 255)
            for num in range(0, 5):
                operator_bd[num].color = (255, 255, 255)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                display.msg = display.msg[0: -1]

            elif event.key == pygame.K_0:
                display.msg += '0'
                button_backdrop[0].color = (100, 100, 100)

            elif event.key == pygame.K_1:
                button_backdrop[1].color = (100, 100, 100)
                display.msg += '1'

            elif event.key == pygame.K_2:
                button_backdrop[2].color = (100, 100, 100)
                display.msg += '2'

            elif event.key == pygame.K_3:
                button_backdrop[3].color = (100, 100, 100)
                display.msg += '3'

            elif event.key == pygame.K_4:
                button_backdrop[4].color = (100, 100, 100)
                display.msg += '4'

            elif event.key == pygame.K_5:
                button_backdrop[5].color = (100, 100, 100)
                display.msg += '5'

            elif event.key == pygame.K_6:
                button_backdrop[6].color = (100, 100, 100)
                display.msg += '6'

            elif event.key == pygame.K_7:
                button_backdrop[7].color = (100, 100, 100)
                display.msg += '7'

            elif event.key == pygame.K_8:
                button_backdrop[8].color = (100, 100, 100)
                display.msg += '8'

            elif event.key == pygame.K_9:
                button_backdrop[9].color = (100, 100, 100)
                display.msg += '9'

            elif event.key == pygame.K_c:
                display.msg = ''

        elif event.type == pygame.KEYUP:
            single_press = True
            for num in range(0, 10):
                button_backdrop[num].color = (255, 255, 255)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        run = False

    win.fill((20, 20, 20))
    for num in range(0, 10):
        button_backdrop[num].draw_back_drop()
        button_num[num].draw_button()

    for num in range(0, 5):
        operator_bd[num].draw_back_drop()
        operator_list[num].draw_button()

    display.draw_button()
    pygame.display.update()

pygame.quit()

