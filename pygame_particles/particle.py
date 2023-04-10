import pygame

from pygame_particles.common import \
    random, np

class Particle:
    def __init__(self, x, y, radius, color):
        self.x = int(x)
        self.y = int(y)
        self.radius = radius
        self.color = color
        self.velocity = 0.1
        self.direction_x = random.randint(0, 5)
        self.direction_y = random.randint(0, 5)
    
    @property
    def vec(self):
        return np.array([self.x, self.y])
    
    @vec.setter
    def vec(self, new_vec: np.ndarray):
        self.x, self.y = new_vec

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.velocity * self.direction_x
        self.y += self.velocity * self.direction_y

        if self.x > 800 or self.x < 0:
            self.direction_x *= -1

        if self.y > 600 or self.y < 0:
            self.direction_y *= -1