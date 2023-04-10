import pygame
import random

from pygame_particles.engine import PygameParticle

def run():
    # create pygame surface and draw
    pygame.init()
    w, h = 800, 600
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Pygame Particles')

    ppart = PygameParticle(w, h, 5000)

    # run game loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        ppart.draw(screen, show_fps=True)
        ppart.update()

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    run()