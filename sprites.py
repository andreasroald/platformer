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

        self.moving = False
        self.left_lock = False
        self.right_lock = False

        self.acceleration = 0
        self.top_speed = 8
        self.velocity = 0

    # Player class event handling
    def events(self):
        #Reset moving & acceleration
        self.moving = False
        self.acceleration = 0

        # Movement keys handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and not self.left_lock:
            self.right_lock = True
            self.moving = True
            self.acceleration = -0.5
            self.accelerate(self.acceleration)
        else:
            self.right_lock = False

        if keys[pygame.K_d] and not self.right_lock:
            self.left_lock = True
            self.moving = True
            self.acceleration = 0.5
            self.accelerate(self.acceleration)
        else:
            self.left_lock = False

        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            if self.velocity != 0:
                self.moving = True
            self.accelerate(self.acceleration)

    #Accelerate the player movement with acc_movement
    def accelerate(self, acc_movement):
        if acc_movement > 0:
            if self.velocity == self.top_speed:
                self.velocity = self.top_speed

            elif acc_movement < self.top_speed:
                self.velocity += acc_movement

        elif acc_movement < 0:
            if self.velocity == -self.top_speed:
                self.velocity = -self.top_speed

            elif acc_movement > -self.top_speed:
                self.velocity += acc_movement

        #If velocity is not 0, slowly make velocity slower
        else:
            if self.velocity != 0:
                if self.velocity > 0:
                    self.velocity -= 0.5
                elif self.velocity < 0:
                    self.velocity += 0.5

    # Update the player class
    def update(self):
        self.events()

        # Make player move
        if self.moving:
            self.rect.x += self.velocity

    # Player drawing function
    def draw(self, display):
        display.blit(self.image, self.rect)
