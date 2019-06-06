import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from time import sleep


class Ship:
    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.settings = settings
        # Retrieve the ship image from the image folder and get its rect.
        self.image = pygame.image.load('text_files/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Have each new ship start at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        # Movement flag for holding down keys.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx


class Alien(Sprite):
    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()  # Extend to child
        self.screen = screen
        self.settings = settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('text_files/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()  # Inherits properties from Sprite
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        # Set color and speed of bullet.
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet and rect position.
        self.y -= self.speed_factor  # Moving bullet up decreases y
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, settings):
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.game_title = 'Alien Invasion'
        # Ship
        self.ship_speed_factor = 3.5
        self.ship_limit = 30
        # Bullet
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30
        # Alien
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 5
        self.fleet_direction = 1  # 1 = right; -1 = left


def run_game():
    """Initialize pygame, setting, screen object, ship object, bullets, aliens, and game title."""
    pygame.init()
    settings = Settings()
    stats = GameStats(settings)
    pygame.display.set_caption(settings.game_title)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    # Create the first fleet of aliens
    create_fleet(settings, screen, ship, aliens)
    while True:
        # Looks for keyboard inputs
        check_events(settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            update_bullets(settings, screen, ship, aliens, bullets)
            update_aliens(settings, stats, screen, ship, aliens, bullets)
            update_screen(settings, screen, ship, aliens, bullets)


def check_events(settings, screen, ship, bullets):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, settings, screen, ship, bullets):
    """Respond to key presses"""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(settings, screen, ship, alien, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen (AKA frame tick)
    screen.fill(settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Delete bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)


def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if limit is not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Check for bullets that have hit the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # Destroy existing bullets and create a new fleet.
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)


def create_fleet(settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_aliens(settings, stats, screen, ship, aliens, bullets):
    """Check if alien is at edge. Update the position of all aliens in the fleet."""
    check_fleet_edges(settings, aliens)
    aliens.update()
    # Look for alien ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False


run_game()
