#All constant values can be found here

import pygame

width = 800 #width of the game board
height = 800 #height of the game board

rows = 8 #no. of rows of the checkers board
columns =8  #mp. of columns of the checkers board

square_size = height//rows #Determining the size of an individual square in the game window

#Colors to be implemented in the UI
color_red = (255, 0 ,0)

color_white = (255, 255, 255)

color_black = (0, 0, 0)

color_green = (0, 255, 0)

color_turqoise = (0, 113, 50)

color_grey = (169, 186, 203)

king_crown =  pygame.transform.scale(pygame.image.load('Checkers\Assets\crown.png'), (40, 20)) #Crown for the king pieces