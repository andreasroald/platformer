import pygame

from settings import *
from sprites import *

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
        # Creating an instance of the player
        self.player = Player()

        # Starting the game loop
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

    # Game loop - Updates
    def update(self):
        self.player.update()

    # Game loop - Draw
    def draw(self):
        self.game_display.fill(white)

        self.player.draw(self.game_display)

        pygame.display.update()

# Creating the game object
game = Game()

# Starting the game loop
while game.running:
    game.new()

pygame.quit()
quit()
