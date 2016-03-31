import pygame

from settings import *

# Player class
class Player(pygame.sprite.Sprite):
    # Initialize the player class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((64, 64))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)

        self.moving_left = False
        self.moving_right = False

        self.speed = 8

    # Player class event handling
    def events(self):
        # Movement keys handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moving_left = True
        else:
            self.moving_left = False

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moving_right = True
        else:
            self.moving_right = False

    # Update the player class
    def update(self):
        self.events()

        # Make player move
        if self.moving_left:
            self.rect.x -= self.speed
        if self.moving_right:
            self.rect.x += self.speed

    # Player drawing function
    def draw(self, display):
        display.blit(self.image, self.rect)
