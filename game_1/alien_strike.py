import sys
from time import sleep

import json
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from meter_bar import Meter, Bars
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()

         #Sets the screen to full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Background Image
        self.background = pygame.image.load('images/background.bmp')

        #Sets the screen to a 1200 by 800 window
        #self.screen = pygame.display.set_mode(
            #(self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption(self.settings.name_game)

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        # Create a scoreboard instance
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.meter = Meter(self)
        self.cover = Meter(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.meter_bar = pygame.sprite.Group()
        self.bars = pygame.sprite.Group()

        self._create_fleet()
        self._create_bars()

        self.play_button = Button(self, "Play")

#Modules for game functionality
#
#

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self.update_cover()
            self._update_screen()


    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Moves the ship to the right or right
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # Button event
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _start_game(self):

        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Resets the game settings
            self.settings.intialize_dynamic_settings()

            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self.settings.intialize_dynamic_settings()
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

# Bullet Modules
#
#

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet position and get rid of old bullets"""
        # Updates bullet position
        self.bullets.update()

        # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collsions()

#Alien Modules
#
#
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a  row"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Makes a fleet of aliens"""
        # Spacing between each alien equal to one alien width
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (alien_width * 2)
        number_aliens_x = available_space_x // (alien_width * 2)

        # Determine the number of rows that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - \
                            (ship_height + 3 * alien_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet
            and check is fleet is at an edge and act accordingly"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for ship-alien collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_bullet_alien_collsions(self):
        """Respond to bullet-alien collisions"""
        # Get rid of aliens and bullets that have collided
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increments level
            self.stats.level += 1
            self.sb.prep_level()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update ships left display
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break



# Meter Modules: This meter measures the number of bullets the ship has
    def _create_bar(self, bar_number):
        """Create a bar and place in its row"""
        self.bar = Bars(self)
        bar_height = self.settings.bar_height
        self.bar.y = 4 + self.settings.meter_y + bar_height * \
                (self.settings.bullets_allowed - 1) - bar_height * bar_number

        self.bar.rect.y = int(self.bar.y)
        self.bars.add(self.bar)

    def _create_bars(self):
        """Makes all the bars"""
        # Create the bars
        for bar_number in range(self.settings.bullets_allowed):
            self._create_bar(bar_number)

    def update_cover(self):
        """Updates the cover to cover up the right bars"""
        self.cover.rect.height = int(len(self.bullets) * self.settings.bar_height)

# Module that updates screen
#
#
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.blit(self.background, [0, 0])

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.meter_bar.add(self.meter)
        for meter in self.meter_bar.sprites():
            meter.draw_meter()
        for bar in self.bars.sprites():
            bar.draw_bar()
        self.cover.draw_meter()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        self.ship.blitme()

        # Draw button if game in not active
        if not self.stats.game_active:
            # Sets new universal high score if it is beat
            if self.stats.high_score > self.stats.uni_high_score:
                filename = "high_score.json"
                with open(filename, 'w') as f:
                    json.dump(self.stats.high_score, f)

            self.play_button.draw_button()
        pygame.display.flip()

# Runs game
#
#
if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


