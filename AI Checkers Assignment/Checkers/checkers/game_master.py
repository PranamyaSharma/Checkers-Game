import pygame
from checkers.board import Board
from .constants import color_red, color_white, color_green, square_size

class Game:
    def init(self):
        self.selected = None
        self.board = Board()
        self.turn = color_red
        self.valid_moves = {}

    def __init__(self, win):
        self.init()
        self.win = win
    
    def get_board(self):
        return self.board

    def ai_move(self, board): #After the AI decides its move, this method returns the new board after the move has been executed
        self.board = board
        self.turn_change() #Changes the turn after the board

    def update(self): #Method to constantly update the game display
        self.board.draw_all(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def reset(self):
        self.init()
    
    def select(self, row, col): #Moves the selected piece to the new position
        if self.selected:
            result = self.move(row, col)
            if not result: #Try to select a different piece if the movement is not allowed
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn: 
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
    
    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves: #If the piece selected is empty and the move is valid
            self.board.move_pieces(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            
            if skipped:
                self.board.remove(skipped)
            self.turn_change()
        else:
            return False
        return True

    def turn_change(self): #Swaps the turns
        self.valid_moves = {}
        if self.turn == color_red:
            self.turn = color_white
        else:
            self.turn = color_red

    def draw_valid_moves(self, moves): #Shows all valid moves
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, color_green,((col * square_size) + square_size //2, (row * square_size) + square_size // 2), 15)

    def winner(self): #Calls the determine winner method from board
        return self.board.determine_winner()

            
