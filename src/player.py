import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED,PLAYER_SPEED, PLAYER_SHOOT_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor, passing in the x,y and player radius
        super().__init__(x, y, PLAYER_RADIUS)

        # Initialize rotation (angle in degrees)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        """Update the player's rotation by adding the turn speed multiplied by dt"""
        self.rotation += PLAYER_TURN_SPEED * dt
    

    def move(self, dt, direction=1):
        """Move the player forward or backward depending on the direction"""
        # Create a unit vector pointing straight up and rotate it by the player's current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Multiply by PLAYER_SPEED and dt, and by direction to go forward (+1) or backward (-1)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        """Fire a shot in the direction the player is facing"""
        shot = Shot(self.position.x, self.position.y, self.rotation)

    def update(self, dt):
        """Update the player's rotation based on input"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            # Move forward with W key
            self.move(dt, direction=1)  # Move forward

        if keys[pygame.K_s]:
            # Move backward with S key
            self.move(dt, direction=-1)  # Move backward

        if keys[pygame.K_a]:
            # Rotate counter-clockwise by passing -dt (invert dt)
            self.rotate(-dt)

        if keys[pygame.K_d]:
            # Rotate clockwise by passing dt
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            # Fire a shot when spacebar is pressed
            self.shoot()
        

    def draw(self, screen):
        """ Draw the player's ship as a white triangle"""
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)