# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids Game")

# Create a Clock object to manage frame rate
clock = pygame.time.Clock()

# Create the player object and place it in the center of the screen
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create groups for updatable and drawable objects
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

# Add player to both groups
updatable.add(player)
drawable.add(player)

# Set the static containers field for the asteroid and AsteroidField Classes
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable) # Shots automatically added to

# Create the AsteroidField object to spawn asteroids
asteroid_field = AsteroidField()

def main():
	""" Main Game Loop """
	# Initialize the delta time (dt) variable
	dt = 0

	# Infinite game loop
	while True:
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 	# Exit the game loop if the user closes the window
		
		# Update all updatable objects
		for obj in updatable:
			obj.update(dt)
		
		# Check for collisions between asteroids and shots
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.is_colliding(shot):
					# Remove both the asteroid and the shot
					asteroid.split()
					shot.kill()

		# Check for collisions between the player and asteroids
		for asteroid in asteroids:
			if player.is_colliding(asteroid):
				print("Game over!")
				pygame.quit()
				return 	# Exit the game

		# Step 3 : Draw everything to the screen
		screen.fill((0, 0, 0 )) 	# Fill the screen with a solid black color
		
		# Draw all drawable objects
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()	# Refresh the screen (update display)

		# Limit the frame rate to 60 FPS and update delta time
		dt = clock.tick(60) / 1000 # Pause the loop to maintain 60 FPS and convert dt to seconds


if __name__ == "__main__":
	main()
