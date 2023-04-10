from pygame_particles import PygameParticle
from pygame_particles.common import random, pygame


if __name__ == "__main__":
    # initialize pygame
    pygame.init()
    w, h = 800, 600
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Basic Pygame Particles')

    # create particle engine
    ppart = PygameParticle(w, h, 500)

    # run game loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # update particles
        ppart.draw(screen, show_fps=True)
        ppart.update()

        pygame.display.flip()
    pygame.quit()



