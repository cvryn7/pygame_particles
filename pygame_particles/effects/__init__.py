from pygame_particles.common import \
    random, pygame, np
from pygame_particles.color import random_color
from pygame_particles import Particle

create_particles = lambda w, h, np: \
    [Particle(random.random()*w, 
        random.random()*h, 5, 
        random_color()) 
    for _ in range(np)]

class ParticleEffect:
    def __init__(self, width: int, height: int, num_particles: int):
        self.w = width
        self.h = height
        self.np = num_particles  # number of particles
        
        self.clock = pygame.time.Clock()
        self.particles = \
            create_particles(self.w, self.h, self.np)
        self.p_vecs = \
            np.array([p.vec for p in self.particles])

    def draw(self, screen):
        self.clock.tick()
        for p in self.particles:
            p.draw(screen)

    def update(self):
        for p in self.particles:
            p.move()

    def update_screen_size(self, width: int, height: int):
        self.w = width
        self.h = height

    def update_num_particles(self, num_particles: int):
        self.np = num_particles