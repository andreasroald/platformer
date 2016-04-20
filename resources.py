import pygame

# -- IMAGES --
player_standing = pygame.image.load("player_sprite_32.png")
player_run_1 = pygame.image.load("player_run_1.png")
player_run_2 = pygame.image.load("player_run_2.png")
player_sprite_jump_3 = pygame.image.load("player_sprite_jump_3.png")

player_list_right = [player_standing, player_run_1, player_run_2]

player_standing_left = pygame.image.load("player_sprite_32_left.png")
player_run_1_left = pygame.image.load("player_run_1_left.png")
player_run_2_left = pygame.image.load("player_run_2_left.png")
player_sprite_jump_3_left = pygame.image.load("player_sprite_jump_3_left.png")

player_list_left = [player_standing_left, player_run_1_left, player_run_2_left]
