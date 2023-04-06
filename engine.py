from common import random, pygame

from color import random_color
from particle import Particle


class PygameParticle:
    def __init__(self, w, h, num_particles: int):
        self.particles = []
        self.w = w
        self.h = h
        self.clock = pygame.time.Clock()
        for _ in range(num_particles):
            self.particles.append(Particle(random.random()*w, 
                                           random.random()*h, 
                                           5, random_color()))
    
    def draw(self, screen, show_fps: bool = False):
        self.clock.tick()
        for p in self.particles:
            p.draw(screen)

        if show_fps:
            font = pygame.font.SysFont("comicsansms", 15)
            text = font.render(f"FPS: {self.clock.get_fps():.2f}", True, (255, 255, 255))
            screen.blit(text, (10, 10))

    def update(self):
        for p in self.particles:
            p.move()