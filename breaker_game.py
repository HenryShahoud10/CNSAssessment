# Import additional modules
import pygame
import random
import webbrowser
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Define celebratory effects (confetti or banner)
celebration_font = pygame.font.Font(None, 72)
celebration_banner_color = (255, 223, 0)  # Gold color for the banner

# Continue existing code for setting up the game
# ...

# Handling game over state
if game_over:
    if win:
        # Celebration effects
        win_text = "You Won, " + player_name + "!"
        win_message = font.render(win_text, True, BLUE_BLACK)
        win_rect = win_message.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(win_message, win_rect)

        # Celebration banner
        pygame.draw.rect(screen, celebration_banner_color, pygame.Rect(50, 100, SCREEN_WIDTH - 100, 100))
        congrats_text = celebration_font.render(f"Congrats {player_name}!", True, BLACK)
        screen.blit(congrats_text, (120, 130))

        # Display confetti or animation (can be customized further)
        # ...
    else:
        game_over_text = font.render("Game Over", True, BLUE_BLACK)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(game_over_text, text_rect)

pygame.display.flip()
