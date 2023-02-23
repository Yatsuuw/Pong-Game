import pygame
from random import randint
BLACK = (0, 0, 0)


# Class
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Set
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Velocity
        self.velocity = [randint(4,8),randint(-8,8)]

        #fetch rectangle
        self.rect = self.image.get_rect()

    # Update
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Bounce
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
