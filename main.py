from Board import *
import random
import math

def printMessage():
    print("Enter number to indicate which game you would like to play (0 to stop)")
    print("0) Stop playing")
    print("1) Tic-Tac-Toe")
    print("2) Connect Four")
    #print("3) Checkers")
    print()

#STILL NEEDS ALPHA-BETA PRUNING
def minimax(game_no, board, depth, engineTurn: bool) -> int:
    if depth == 0 or board.gameComplete(game_no): 
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
    depth = 10 
    b = Board(3, 3)
    
    engineTurn = random.randint(0,1) == 1
    
    print("\nGAME BOARD")
    print('+---+---+---+')
    print('| 1 | 2 | 3 |')
    print('+---+---+---+')
    print('| 4 | 5 | 6 |')
    print('+---+---+---+')
    print('| 7 | 8 | 9 |')
    print('+---+---+---+\n')


    if engineTurn:
        print("Engine making first move\n\n")
    else:
        print("Player making first move\n\n")
    
    while b.gameComplete(1) == False:
        if engineTurn:
            children = b.getChildren(1, True)
            bestEval = minimax(1, b, depth, True)

            if len(children) != 9: #For starting move we should start on a corner every time
                random.shuffle(children) #Engine is no longer deterministic

            else:
                new_children = [children[0], children[2], children[6], children[8]]
                random.shuffle(new_children)
                #We will randomly pick which corner to choose if we go first
                children = new_children

            for child in children:
                eval = minimax(1, child, depth-1, False)
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

def tester():
    b = Board(6, 7)
    engineTurn = False

    if False: # / test
        b.changeVal(5, 0, 'x')
        b.changeVal(4, 1, 'x')
        b.changeVal(3, 2, 'x')

        b.changeVal(5, 3, 'o')
        b.changeVal(4, 3, 'o')
        b.changeVal(3, 3, 'o')

    if True: # \ test
        b.changeVal(5, 3, 'x')
        b.changeVal(4, 2, 'x')
        b.changeVal(3, 1, 'x')

        b.changeVal(5, 0, 'o')
        b.changeVal(4, 0, 'o')
        b.changeVal(3, 0, 'o')

    while b.gameComplete(2) == False:
        
        col = int(input("What column to place piece: ").strip()) - 1
        b.dropPiece(col, engineTurn)
        print(b, end = "\n\n")
        #engineTurn = not engineTurn

    print("Game over")
    print(b)




def connect4():
    depth = 6

    print("\nGAME BOARD\n")
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
    print('+---+---+---+---+---+---+---+')
    print('|   |   |   |   |   |   |   |')
    print('+---+---+---+---+---+---+---+')
    print('|   |   |   |   |   |   |   |')
    print('+---+---+---+---+---+---+---+')
    print('| : | : | : | : | : | : | : |')
    print('+---+---+---+---+---+---+---+')
    print('|   |   |   |   |   |   |   |')
    print('+---+---+---+---+---+---+---+\n')


    b = Board(6, 7)
    engineTurn = random.randint(0,1) == 1

    if engineTurn:
        print("Engine making first move\n\n")
    else:
        print("Player making first move\n\n")



    while b.gameComplete(2) == False:
        if engineTurn:
            children = b.getChildren(2, True)
            bestEval = minimax(2, b, depth, True)

            
            random.shuffle(children) #Engine is no longer deterministic


            for child in children:
                eval = minimax(2, child, depth-1, False)
                if eval >= bestEval:
                    bestMove = child
                    break
            b = bestMove

        else: # user turn
            print(b)
            col = int(input("what col would you like to place your piece: ").strip()) - 1
            b.dropPiece(col)

        
        engineTurn = not engineTurn


    print("Game Over")
    print(b)


if __name__ == "__main__":   
    printMessage()
    game_no = int(input("Enter the number of game you would like to play: ").strip())

    while(game_no != 0):
        game_no = 3
        if game_no == 1:
            tictactoe()

        elif game_no == 2:
            connect4()

        elif game_no == 3:
            tester()

        printMessage()
        game_no = int(input("Enter number of game you would like to play: ").strip())
    
    print("Thanks for playing!")