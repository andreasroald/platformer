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

        self.max_speed = 8

        self.acceleration = 0

    # Player class event handling
    def events(self):
        #Reset moving
        self.moving = False
        speed = 0
        
        # Movement keys handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moving = True
            speed = -0.5
            self.accelerate(speed)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moving = True
            speed = 0.5
            self.accelerate(speed)

        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            if self.acceleration != 0:
                self.moving = True
            self.accelerate(speed)

    #Accelerate the player movement with acc_movement
    def accelerate(self, acc_movement):
        if acc_movement > 0:
            if self.acceleration == self.max_speed:
                self.acceleration = self.max_speed
                
            elif acc_movement < self.max_speed:
                self.acceleration += acc_movement

        elif acc_movement < 0:
            if self.acceleration == -self.max_speed:
                self.acceleration = -self.max_speed
                
            elif acc_movement > -self.max_speed:
                self.acceleration += acc_movement

        #If acceleration is 0, slowly make acceleration slower        
        else:
            if self.acceleration != 0:
                if self.acceleration > 0:
                    self.acceleration -= 0.5
                elif self.acceleration < 0:
                    self.acceleration += 0.5  

    # Update the player class
    def update(self):
        self.events()

        # Make player move
        if self.moving:
            self.rect.x += self.acceleration

    # Player drawing function
    def draw(self, display):
        display.blit(self.image, self.rect)
