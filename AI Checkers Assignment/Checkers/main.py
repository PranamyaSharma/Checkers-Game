from distutils.log import debug
import pygame
import sys
from checkers.constants import width, height, square_size, color_red, color_white
from checkers.game_master import Game
from Minimax.minimax_algo import minimax

pygame.init()
fps = 60 #Setting the frames per second of the clock

win = pygame.display.set_mode((width, height)) #Game window
pygame.display.set_caption('Checkers Game') #Setting the caption to be seen

def main(): #The main function to run for the program
    run = True
    clock = pygame.time.Clock() # A clock for the game to maintain speed without regard to the speed of the computer
    # board = Board() #Creating a new board
    game = Game(win)

    while run == True:
        clock.tick(fps)

        if game.turn == color_white:
            value, new_board = minimax(game.get_board(), 3, color_white, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.win())
            run  = False #Ends the game once a winner is determined
        
        for event in pygame.event.get(): #Creating an event loop tp check to see if any events have happened at the current time
            if event.type == pygame.QUIT: #Ends the loop if the quit button is pressed
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #If the mouse button is pressed
                position = pygame.mouse.get_pos()
                row, column = get_pos_mouseclick(position)
                game.select(row, column)
        
        game.update()

    pygame.quit() #The game is quit if the whileloop stops

def get_pos_mouseclick(mouse_position): #Returns the position of the selected piece through the mouse position
    x, y =  mouse_position
    row = y // square_size
    column = x // square_size
    return row, column
    
main()  