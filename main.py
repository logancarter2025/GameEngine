from Board import *
import random
import math

def printMessage():
    print("Enter number to indicate which game you would like to play (-1 to stop)")
    print("0) Stop playing")
    print("1) Tic-Tac-Toe")
    print("2) Connect Four")
    print("3) Checkers")


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
    
    engineTurn = False
    if random.randint(0,1) == 1:
        engineTurn = True
    
    if engineTurn:
        print("Engine making first move")
    else:
        print("Player making first move")

    while b.gameComplete(1) == False:
        if engineTurn:
            children = b.getChildren(1, True)
            bestMove = children[0]
            bestEval = minimax(1, bestMove, 9, False)
            for child in children:
                eval = minimax(1, child, 9, False)
                if eval > bestEval:
                    bestMove = child
                    bestEval = eval
            b = bestMove

        else: # user turn
            print(b)
            row_no = int(input("what row would you like to place your piece: ").strip)
            col_no = int(input("what col would you like to place your piece: ").strip)
            b.changeVal(row_no, col_no, 'x')
        
        engineTurn = not engineTurn

    


if __name__ == "__main__":   
    for i in range(100):
        print(random.randint(0,1)) 
    printMessage()
    game_no = int(input("Enter number of game you would like to play: ").strip())

    while(game_no != 0):
        

        if game_no == 1:
            print("You are now playing tic-tac-toe")
            tictactoe()

        printMessage()
        game_no = int(input("Enter number of game you would like to play: ").strip())
    
    print("Thanks for playing!")