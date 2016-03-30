import pygame

from settings import *

# Create the game class
class Game:
    # Initialize the game class
    def __init__(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True # To exit the game completely, make running False

    # Starting a new game
    def new(self):
        self.loop()

    # Game loop
    def loop(self):
        self.playing = True # To reset the game, but not close it, make playing False
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    # Game loop - Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    # Game loop - Updates
    def update(self):
        pass

    # Game loop - Draw
    def draw(self):
        self.game_display.fill(white)
        pygame.display.update()

# Creating the game object
game = Game()

# Starting the game loop
while game.running:
    game.new()

pygame.quit()
quit()
