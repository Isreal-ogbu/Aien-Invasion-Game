import sys
import pygame
from bullet import Bullet
from aliens import Alien
from time import sleep


def check_fleet_edges(a1_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(a1_settings, aliens)
            break


def change_fleet_direction(a1_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += a1_settings.fleet_drop_speed
    a1_settings.fleet_direction *= -1


def ship_hit(a1_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left = -1
        aliens.empty()
        bullets.empty()
        create_fleet(a1_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(a1_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(a1_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(a1_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(a1_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(a1_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(a1_settings, stats, screen, ship, aliens, bullets)


def get_number_of_aliens(a1_settings, alien_width):
    available_space = a1_settings.screen_width - 2 * alien_width
    number_aliens = int(available_space / (2 * alien_width))
    return number_aliens


def get_number_rows(a1_settings, ship_height, alien_height):
    available_space_y = (a1_settings.screen_height - (3 * alien_height)-ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows


def create_aliens(a1_settings, screen, aliens, alien_number, row_number):
    alien = Alien(a1_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(a1_settings, screen, ship,  aliens):
    alien = Alien(a1_settings, screen)
    number_aliens = get_number_of_aliens(a1_settings, alien.rect.width)
    number_rows = get_number_rows(a1_settings, ship.rect.height, alien.rect.height)
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            create_aliens(a1_settings, screen, aliens, alien_number, row_number)


def check_keydown_events(event, a1_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(a1_settings, screen, ship, bullets)


def fire_bullet(a1_settings, screen, ship, bullets):
    if len(bullets) < a1_settings.bullets_allowed:
        new_bullet = Bullet(a1_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_event(a1_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(a1_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, a1_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(a1_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        a1_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()

        create_fleet(a1_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(a1_settings, screen, ship, stats, score_board, aliens, bullets, play_button):
    screen.fill(a1_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score_board.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(a1_settings, screen, stats, score_board, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_collisions(a1_settings, screen, stats, score_board, ship, aliens, bullets)


def check_bullet_collisions(a1_settings, screen, stats, score_board, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += a1_settings.alien_points * len(aliens)
            score_board.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        a1_settings.increase_speed()
        create_fleet(a1_settings, screen, ship, aliens)
