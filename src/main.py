# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

# Initialize Pygame
pygame.init()


# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids Game")

def main():
	""" Main Game Loop """
	# Infinite game loop
	while True:
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 	# Exit the game loop if the user closes the window
		# Step 3 : Draw everything to the screen
		screen.fill((0, 0, 0 )) 	# Fill the screen with a solid black color
		
		pygame.display.flip()	# Refresh the screen (update display)

if __name__ == "__main__":
	main()
