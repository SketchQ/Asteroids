import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class's constructor
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        """Draw the asteroid as a circle"""
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        """Update the asteroid's position based on its velocity."""
        self.position += self.velocity * dt

    def split(self):
        """Split the asteroid into two smaller ones or destroy it if it's too small"""
        # If the asteroid is small, just destroy it
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        # Kill this asteroid (remove it)
        self. kill()

        # Generate a random angle between 20 and 50 degrees for the split
        random_angle = random.uniform(20, 50)

        # Compute the new velocity vectors for the smaller asteroids
        velocity1 = self.velocity.rotate(random_angle) * 1.2 # Slightly faster
        velocity2 = self.velocity.rotate(-random_angle) * 1.2 # Slightly faster

        # New radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two smaller asteroids at the current position with new velocities
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = velocity1

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = velocity2
        