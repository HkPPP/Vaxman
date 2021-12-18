#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from game import Game

# VAXMAN RULES:

# Checked: Vax-Man can kill a ghost if he comes into contact with it (vaccinates it).
# Checked: Contact with a ghost does not kill Vax-Man.
# Checked: Each ghost that has not yet been hit multiplies itself every 30 seconds (the infection grows).
# Checked: The goal of the game is to collect all the dots before the number of ghosts grows to 32 times the original number.

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("VAXMAN")
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
    # -------- Main Program Loop -----------
    while not done:
        # --- Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        # --- Game logic should go here
        game.run_logic()
        # --- Draw the current frame
        game.display_frame(screen)
        # --- Limit to 30 frames per second
        clock.tick(60)
        #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':
    main()
