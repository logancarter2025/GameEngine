from Board import *
import random
import math

def printMessage():
    print("Enter number to indicate which game you would like to play (-1 to stop)")
    print("0) Stop playing")
    print("1) Tic-Tac-Toe")
    #print("2) Connect Four")
    #print("3) Checkers")

def minimax(game_no, board, depth, engineTurn: bool) -> int:
    if depth == 0 or board.gameComplete(1): 
        return board.evalGame(game_no)
    
    if engineTurn:
        maxEval = -math.inf
        children = board.getChildren(game_no, True)
        for child in children:
            eval = minimax(game_no, child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    
    else:
        minEval = math.inf
        children = board.getChildren(game_no, False)
        for child in children:
            eval = minimax(game_no, child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
        

def tictactoe():
    b = Board(3, 3)
    
    engineTurn = False
    if random.randint(0,1) == 1:
        engineTurn = True
    

    #engineTurn = True
    if engineTurn:
        print("Engine making first move")
    else:
        print("Player making first move")
    print()
    
    while b.gameComplete(1) == False:
        if engineTurn:
            children = b.getChildren(1, True)
            print("I have", len(children), "children")
            bestEval = minimax(1, b, 10, True)
            for child in children:
                eval = minimax(1, child, 10, False)
                if eval >= bestEval:
                    bestMove = child
                    break
            b = bestMove

        else: # user turn
            print(b)
            space = int(input("where would you like to place your piece: ").strip()) - 1
            b.changeVal(space//3, space%3, 'x')
        
        engineTurn = not engineTurn

    print("Game Over")
    print(b)

def simulation():
    for x in range(100):
        b = Board(3,3)
        for i in range(3):
            for j in range(3):
                r = random.randint(1,2)
                if r == 1:
                    b.changeVal(i, j, 'o')

                else:
                    b.changeVal(i, j, 'x')

                if b.gameComplete(1):
                    break

            if b.gameComplete(1):
                    break

        print(b.evalGame(1))
        print(b)
        


if __name__ == "__main__":   
    printMessage()
    game_no = int(input("Enter number of game you would like to play: ").strip())

    while(game_no != 0):

        if game_no == 1:
            #print("You are now playing tic-tac-toe")
            tictactoe()

        printMessage()
        game_no = int(input("Enter number of game you would like to play: ").strip())
    
    print("Thanks for playing!")