from pygame_particles.common import \
    random, pygame, ParticleEffect, np

from pygame_particles.color import random_color
from pygame_particles.particle import Particle


class PygameParticle:
    def __init__(self, width: int, height: int, num_particles: int):
        self.w = width
        self.h = height
        self.np = num_particles  # number of particles
        self.effect = ParticleEffect(self.w, self.h, num_particles)
    
    def draw(self, screen, show_fps: bool = False):
        self.effect.draw(screen)

        if show_fps:
            font = pygame.font.SysFont("comicsansms", 15)
            text = font.render(f"FPS: {self.clock.get_fps():.2f}", True, (255, 255, 255))
            screen.blit(text, (10, 10))

    def update(self):
        self.effect.update()