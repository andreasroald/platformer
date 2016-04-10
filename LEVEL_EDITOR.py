import pygame
import random

from settings import *


class Wall(pygame.sprite.Sprite):
    # Initialize the wall class
    def __init__(self, x, y, w=32, h=32, color=black, image=None):
        pygame.sprite.Sprite.__init__(self)
        if image is None:
            self.image = pygame.Surface((w, h))
            self.image.fill(color)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Editor:
    # Initialize the editor
    def __init__(self):
        pygame.init()

        # Ask for level width and level height, make the level 25x20 tiles (800x640px)
        # if non-valid value is entered
        try:
            self.display_width = int(input("Enter the level width: ")) * 32
        except (ValueError, EOFError):
            self.display_width = 25 * 32

        try:
            self.display_height = int(input("Enter the level height: ")) * 32
        except (ValueError, EOFError):
            self.display_height = 20 * 32

        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("LEVEL EDITOR v3")

        # Framerate
        self.clock = clock = pygame.time.Clock()
        self.FPS = 60

        self.running = True

    # Get the coordinates of each tile
    def get_coordinates(self):
        coord_list = []

        for x in range(0, int(self.display_height / 32)):
            for y in range(0, int(self.display_width / 32)):
                coord_list.append((y*32, x*32))
        return coord_list

    # Starting a new game
    def new(self):
        self.coordinates = self.get_coordinates()
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        self.output_level = []

        # Appending the amount of rows to output_level
        for x in range(int(self.display_height / 32)):
            self.output_level.append([])

            for y in range(int(self.display_width / 32)):
                self.output_level[x].append(0)

        self.walls = pygame.sprite.Group()

        self.run()

    # Game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

    # Game loop - Events
    def events(self):
        # --- KEYBOARD AND QUIT EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.walls.empty()
                # Printing the level
                if event.key == pygame.K_RETURN:
                    for coords in self.coordinates:
                        for w in self.walls:
                            if w.rect.x == coords[0] and w.rect.y == coords[1]:
                                self.output_level[int(coords[1]/32)][int(coords[0]/32)] = 1

                    print("YOUR LEVEL:")
                    for level in self.output_level:
                        print("{},".format(level))


        # --- MOUSE EVENTS ---
        # Tile placement
        if self.click[0]:
            for x in self.coordinates:
                if x[0] < self.mouse_x < x[0] + 32:
                    if x[1] < self.mouse_y < x[1] + 32:
                        # Erasing any previous tiles at this location
                        for w in self.walls:
                            if w.rect.x == x[0] and w.rect.y == x[1]:
                                self.walls.remove(w)
                                break

                        w = Wall(x[0], x[1])
                        self.walls.add(w)
                        break

        # Tile erasing
        if self.click[2]:
            for x in self.coordinates:
                if x[0] < self.mouse_x < x[0]+32:
                    if x[1] < self.mouse_y < x[1]+32:
                        for w in self.walls:
                            if w.rect.x == x[0] and w.rect.y == x[1]:
                                self.walls.remove(w)
                                break

    # Game loop - Update
    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    # Game loop - Rendering/Drawing
    def draw(self):
        self.game_display.fill(white)

        self.walls.draw(self.game_display)

        pygame.display.update()

# Creating the game window
e = Editor()

while e.running:
    e.new()

pygame.quit()
quit()
