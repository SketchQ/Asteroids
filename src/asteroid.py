import pygame
from circleshape import CircleShape

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