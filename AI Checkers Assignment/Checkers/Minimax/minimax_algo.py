import pygame 

from copy import deepcopy #To copy not only the reference but the object itself

color_red = (255, 0, 0)
color_white = (255, 255, 255)

def minimax(position, depth, max_player, game): # Position: Current state of the board, depth: how far to extend the tree, max_player(true) causes maximization else minimization
    print (position.white_king)
    if (depth == 0 or position.determine_winner() != None):
        return position.evaluate_board(), position
    if max_player: #To maximize the score
        maxEval = float('-inf') #The maximum starts at negative infinity as nothing has been evaluated yet
        best_move = None
        for move in get_all_moves(position, color_white, game): #Gets all the possible moves for the current position/state of the board, maximizing player is white
            evaluation = minimax(move, depth-1, False, game)[0] #Evaluate the move
            maxEval = max(maxEval, evaluation) #Changes the move if and only if it is better
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else: #To minimize the score
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, color_red, game): 
            evaluation = minimax(move, depth-1, True, game)[0] 
            minEval = max(minEval, evaluation) 
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
 
def get_all_moves(board, color, game): #Check all the moves for all pieces
    moves = []
    for piece in board.get_pieces_all(color):
        valid_moves = board.get_valid_moves(piece) 
        for move, skip in valid_moves.items():
            temp_board =  deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.column)
            new_board = move_simulation(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def move_simulation(piece, move, board, game, skip): 
    board.move_pieces(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board 