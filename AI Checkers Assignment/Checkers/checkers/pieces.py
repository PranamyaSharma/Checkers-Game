import pygame
from .constants import color_red, color_white, square_size, color_black, king_crown

class Pieces:

    piece_padding = 15 #Padding between the piece and the square it is inside
    piece_border = 3 #Border for the piece

    def __init__(self, row, column, color): #When a new piece is made, its row, column and color is passed
        self.row = row
        self.column = column
        self.color = color
        self.is_king = False
        
        self.x = 0
        self.y = 0
        self.calc_position()
    
    def calc_position(self): #Calculates the x and y position of the piece based on the row and column it is in
        self.x = square_size * self.column + square_size // 2
        self.y = square_size * self.row + square_size // 2
    
    def make_king(self): #Makes the piece a king piece
        if self.is_king == False:
            self.is_king = True

    def draw_piece(self, win): #Draws a circle to represent the piece
        piece_radius = square_size // 2 - self.piece_padding
        pygame.draw.circle(win, color_black, (self.x, self.y), piece_radius + self.piece_border)
        pygame.draw.circle(win, self.color, (self.x, self.y), piece_radius)
        if(self.is_king):
            win.blit(king_crown, (self.x - king_crown.get_width() // 2, self.y - king_crown.get_height() // 2)) #Placing the crown in the piece if it is a king piece

    def move(self, row, column): #Moves the piece to the specified row/column
        self.row = row
        self.column = column
        self.calc_position()
        
