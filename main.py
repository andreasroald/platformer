import pygame

from settings import *
from sprites import *
from levels import *

# Create the game class
class Game:
    # Initialize the game class
    def __init__(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True # To exit the game completely, make running False

    # Function that creates a level from a list
    def create_level(self, level):
        level_x = 0
        level_y = 0
        for rows in level:
            for cols in rows:
                if cols == 1:
                    w = Wall(level_x, level_y, 32, 32)
                    self.walls.add(w)

                level_x += 32
            level_x = 0
            level_y += 32

    # Starting a new game
    def new(self):
        # Sprite groups
        self.walls = pygame.sprite.Group()

        # Creating an instance of the player
        self.player = Player(self.walls)

        # Create the level
        self.create_level(level)

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
                    self.player.jump()

    # Game loop - Updates
    def update(self):
        self.player.update()

        # Reset game if player is out of the screen
        if self.player.rect.x < -64:
            self.playing = False
        elif self.player.rect.x > display_width:
            self.playing = False
        elif self.player.rect.y > display_height+64:
            self.playing = False

    # Game loop - Draw
    def draw(self):
        self.game_display.fill(white)

        self.player.draw(self.game_display)
        self.walls.draw(self.game_display)

        pygame.display.update()

# Creating the game object
game = Game()

# Starting the game loop
while game.running:
    game.new()

pygame.quit()
quit()
