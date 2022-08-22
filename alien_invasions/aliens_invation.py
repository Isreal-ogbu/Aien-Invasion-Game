import pygame
from pygame.sprite import Group
from setings import settings
from Game_stats import Gamestats
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen mode
    pygame.init()
    a1_settings = settings()

    # To display window called screen
    screen = pygame.display.set_mode((a1_settings.screen_width, a1_settings.screen_height))
    # Set background color
    # bg_color = (230,230,230)

    pygame.display.set_caption("ALIEN INVASION")
    play_button = Button(a1_settings, screen, 'play')
    stats = Gamestats(a1_settings)
    ship = Ship(a1_settings, screen)
    score_board = Scoreboard(a1_settings, screen, stats)
    # alien = Alien(a1_settings, screen)
    bullets = Group()
    aliens = Group()

    # creating a fleet of aliens
    gf.create_fleet(a1_settings, screen, ship, aliens)

    while True:
        gf.check_event(a1_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            # I changed it from bg_color to color
            screen.fill(a1_settings.bg_color)
            ship.blitme()
            bullets.update()
            gf.update_bullets(a1_settings, screen, stats, score_board, ship, aliens, bullets)
            gf.update_aliens(a1_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(a1_settings, screen, ship, stats, score_board, aliens, bullets, play_button)
        # To display currently drawn object on the screen
        pygame.display.flip()


run_game()
