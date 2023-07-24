from Board import *
import random
import math

def printMessage():
    print("Enter number to indicate which game you would like to play")
    print("1) Tic-Tac-Toe")

def minimax(game_no, board, depth, engineTurn: bool) -> int:
    if depth == 0: 
        return board.evalGame(game_no)
    
    if engineTurn:
        maxEval = -math.inf
        children = board.getChildren(game_no, engineTurn)
        for child in children:
            eval = minimax(game_no, child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    
    else:
        minEval = math.inf
        children = board.getChildren(game_no, engineTurn)
        for child in children:
            eval = minimax(game_no, child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
        

def tictactoe():
    b = Board(3, 3)
    children = b.getChildren(1, True)
    for x in children:
        print(x)
        print()

if __name__ == "__main__":
    
    printMessage()
    game_no = int(input("Enter number of game you would like to play: ").strip())

    if game_no == 1:
        print("You are now playing tic-tac-toe")
        tictactoe()
    