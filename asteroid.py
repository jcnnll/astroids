import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        a1 = self.velocity.rotate(angle)
        a2 = self.velocity.rotate(-angle)

        rad = self.radius - ASTEROID_MIN_RADIUS
        ast = Asteroid(self.position.x, self.position.y, rad)
        ast.velocity = a1 * 1.2
        ast = Asteroid(self.position.x, self.position.y, rad)
        ast.velocity = a2 * 1.2

