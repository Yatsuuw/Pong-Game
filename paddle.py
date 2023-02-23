import pygame
BLACK = (0, 0, 0)

# Class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Set
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch rectangle
        self.rect = self.image.get_rect()

    # Moving up
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    # Moving down
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400
