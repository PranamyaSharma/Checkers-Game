import pygame
from .constants import color_black, color_grey, color_white, square_size, rows, columns, color_red, color_turqoise
from .pieces import Pieces

class Board: #Class that represents the game board
    def __init__(self):
        self.board = [] #Stores the pieces in a 2 dimensional list
        self.red_remaining = 12 #Number of red pieces remaining 
        self.white_remaining =12 #Number of white pieces remaining
        self.red_king = 0
        self.white_king = 0
        self.create_board()

    def draw_squares(self, win): #Draws the checkerbox squares in the window
        win.fill(color_turqoise)
        for row in range(rows):
            for col in range(row % 2, columns, 2):
                pygame.draw.rect(win, color_grey, (row * square_size , col * square_size, square_size, square_size))

    def create_board(self): #Creates a representation of the board and add the pieces to it
        for row in range(rows):
            self.board.append([]) #Interior list for each row
            for col in range(columns):
                if col % 2 == (row + 1) % 2: #Draw the pieces alternately
                    if row <= 2:
                        self.board[row].append(Pieces(row, col, color_white)) #White pieces are only created in the top 3 rows
                    elif row >= 5:
                        self.board[row].append(Pieces(row, col, color_red)) #Red pieces are only created in the bottom 3 rows
                    else:
                        self.board[row].append(0) #Adds a "blank" piece
                else:
                    self.board[row].append(0)

    def draw_all(self, win): #Draws the board and the individual pieces
        self.draw_squares(win)
        for row in range(rows):
            for col in range(columns):
                piece =  self.board[row][col]
                if (piece != 0):
                    piece.draw_piece(win)

    def move_pieces(self, piece, row, column): #Moves a piece to the specified row and column
        self.board[piece.row][piece.column], self.board[row][column] = self.board[row][column], self.board[piece.row][piece.column] #Swapping the values of the piece that is to be moved and the empty piece that is in the place of the destination
        piece.move(row, column)

        if row == 0 or row == rows - 1: #Makes the piece a king if it touches the top or bottom row
            
            if piece.color == color_white:
                if piece.is_king == False:
                    self.white_king += 1
            else:
                if piece.is_king == False:
                    self.red_king += 1
            piece.make_king()

    def get_piece(self, row, column):
        return self.board[row][column]

    def get_valid_moves(self, piece):
        moves = {} #Stores moves as the key and the piece to jump to
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row
        if piece.color == color_red or piece.is_king:
            moves.update(self.traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == color_white or piece.is_king:
            moves.update(self.traverse_left(row + 1, min(row + 3, rows), 1, piece.color, left))
            moves.update(self.traverse_right(row + 1, min(row + 3, rows), 1, piece.color, right))

        return moves
    
    def traverse_left(self, start, stop, step, color, left, skipped = []): #Determines where a player can move to
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0: #Prevents going out of bounds
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] =  last + skipped  
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, rows)

                    moves.update(self.traverse_left(r + step, row, step, color, left-1,skipped = last))
                    moves.update(self.traverse_right(r + step, row, step, color, left+1,skipped = last))
                break

            elif current.color == color:
                break

            else:
                last = [current]

            left -= 1
        return moves

    def traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= columns: #Prevents going out of bounds
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] =  last + skipped  
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, rows)

                    moves.update(self.traverse_left(r + step, row, step, color, right-1,skipped = last))
                    moves.update(self.traverse_right(r + step, row, step, color, right+1,skipped = last))
                break

            elif current.color == color:
                break

            else:
                last = [current]

            right += 1
        return moves
    
    def remove(self, pieces): #Removes skipped pieces from the game
        for piece in pieces:
            self.board[piece.row][piece.column] = 0
            if piece != 0:
                if piece.color == color_red: #Reduces the amount of pieces of a particlar color left if the pieces are captured
                    self.red_remaining -= 1
                else:
                    self.white_remaining -= 1

    def determine_winner(self): #Determines the winner
        if self.red_remaining <= 0:
            return color_white
        elif self.white_remaining <=0:
            return color_red
        
        return None
    
    def evaluate_board(self): #Given the state of the board, determines its score
        return (self.white_remaining - self.red_remaining) + ((self.white_king * 1.5) - (self.red_king * 1.5)) #Determining the score through the number of red and white pieces ramaining, as well as the number of kings remaining
    
    def get_pieces_all(self, color): #Returns all the pieces of a certain color
        pieces = [] #Array to store the pieces of a particular color
        for row in self.board:
            for piece in row:
                if piece !=0 and piece.color == color:
                    pieces.append(piece)
        return pieces
         

        


