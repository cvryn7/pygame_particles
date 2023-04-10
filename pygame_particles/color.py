from pygame_particles.common import random

def random_color():
    def rnd_rgb():
        return random.randint(0, 255)
    return (rnd_rgb(), rnd_rgb(), rnd_rgb())