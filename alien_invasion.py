import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import Gamestats
from button import Buttons
from pygame.time import Clock
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    stats = Gamestats(ai_settings)
    bullets = Group()
    aliens = Group()
    play_button = Buttons(ai_settings, screen, "Play")
    clock = Clock()
    sb = Scoreboard(ai_settings, screen, stats)

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        # Update game objects only if the game is active
        if stats.game_active:

            # Update ship position
            ship.update()

            # Update bullets
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # Update aliens
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        # Limit the frame rate to 200 FPS
        clock.tick(200)

run_game()
