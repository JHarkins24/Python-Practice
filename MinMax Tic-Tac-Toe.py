# Lab 7
# Authors: @Min Ahn @Pierre Smith @Joe Harkins
# October 8, 2020


class Board:
    def __init__(self, board, x_turn, turns):
        self.board = board
        self.x_turn = x_turn
        self.turns = turns

    def getMoves(self):
        possibleMoves = []
        index = 0
        while index < len(self.board):
            if self.board[index] == '-':
                possibleMoves.append(index)
            index += 1
        return possibleMoves

    def makeMove(self, move):
        if self.x_turn:
            self.board[move] = 'X'
            self.x_turn = False
            self.turns += 1
        else:
            self.board[move] = 'O'
            self.x_turn = True
            self.turns += 1

    def undo(self,move):
        self.board[move] = '-'
        self.x_turn = not self.x_turn
        self.turns -= 1

    def __repr__(self):
        boardString = "\n"
        j = 0
        for i in range(0, 9):  # for (i = 0; i < 9; i++)
            boardString += str(self.board[i])
            boardString += ' '
            j += 1
            if j % 3 == 0:
                boardString += "\n"
        return boardString

def GetBestMove(current_board):
    bestScore = float("-inf")
    bestMove = None
    for move in current_board.getMoves():
        current_board.makeMove(move)
        score = MiniMax(current_board)
        current_board.undo(move)
        if(score > bestScore):
            bestScore = score
            bestMove = move

    current_board.makeMove(bestMove)
    return bestMove


def GameOver(current_board):
    winning_combos = [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]

    for combo in winning_combos:
        winner = current_board.board[combo[0]]
        if winner == 'X' or winner == 'O':
            if winner == current_board.board[combo[1]] and winner == current_board.board[combo[2]]:
                if winner == 'X':
                    return 1
                else:
                    return -1

    if current_board.turns == 9:
        return 0

    return '-'

def MiniMax(current_board):
    if GameOver(current_board) != '-':
        return GameOver(current_board)
    else:
        if current_board.x_turn:
            best = float('-inf')
            for move in current_board.getMoves():
                current_board.makeMove(move)
                best = max(best, MiniMax(current_board))
                current_board.undo(move)
            return best
        else:
            best = float('inf')
            for move in current_board.getMoves():
                current_board.makeMove(move)
                best = min(best, MiniMax(current_board))
                current_board.undo(move)
            return best


#~~~~~~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
board = Board(['-', '-', '-', '-', '-','-', '-', '-', '-'], True, 0)
print(board)
print (GetBestMove(board))

board = Board(['X', 'O', 'X', 'O', 'O','X', '-', '-', '-'], True, 0)
print(board)
print (GetBestMove(board))




