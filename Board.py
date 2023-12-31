import copy
import math

class Board(object):
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.board = [  ]
        row = []
        for i in range(numCols):
            row.append(' ')
        for i in range(numRows):
            self.board.append(row[:])
    
    #Returns current state of boards
    def getBoard(self):
        return self.board

    #Copeis board given another board
    def setBoard(self, otherBoard):
        self.board = [row[:] for row in otherBoard]

    #Hashes board
    def hash(self) -> int:
        s = ""
        for i in range(self.numRows):
            s += ''.join([item for item in self.board[i]])
            s += "\n"

        return hash(s)

    #Sets up initial board for checkers game
    def checkersPlacePieces(self):
        for i in range(3):
            for j in range(self.numCols):
                if (i + j)%2 == 1:
                    self.changeVal(i, j, 'o')
        
        for i in range(5, 8):
            for j in range(self.numCols):
                if (i + j)%2 == 1:
                    self.changeVal(i, j, 'x')
        print(self)
        
    #Returns True if the user move is valid for checkers, False otherwise
    def checkersValidMove(self, row, col, row_move, col_move):
        return True

    #Used for games where initial state of board has pieces placed
    def place_pieces(self, game_no):
        if game_no == 3: #checkers
            self.checkersPlacePieces()
                
    def new_copy(self):
        new = Board(self.numRows, self.numCols)
        new.setBoard(self.board)
        return new

    #used for Connect-4
    def dropPiece(self, col: int, engineTurn: bool) -> None:
        for i in range(self.numRows - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = 'o' if engineTurn else 'x'
                break

    def __str__(self):
        s = ''
        for i in range(self.numRows):
            for j in range(self.numCols):
                s += "+---"
            s += '+\n'
            for j in range(self.numCols):
                s += "| " + self.board[i][j] + " "

            s += '|\n'

        for i in range(self.numCols):
            s += "+---"
        s += '+\n'

        return s

    def changeVal(self, row: int, col: int, newVal):
        self.board[row][col] = newVal

    def getVal(self, row: int, col: int, newVal):
        return self.board[row][col]

    def getChildren(self, game_no: int, engineTurn: bool) -> list:
        if game_no == 1:
            return self.tictactoeChildren(engineTurn)
        elif game_no == 2:
            return self.connect4children(engineTurn) 
        elif game_no == 3:
            return self.checkersChildren(engineTurn)
        else:
            return []

    def tictactoeChildren(self, engineTurn: bool) -> list: 
        children = []

        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == ' ':
                    child = self.new_copy()

                    '''
                    for k in range(self.numRows):
                        for l in range(self.numCols):
                            child.changeVal(k, j, self.board[k][l])
                    '''

                    if engineTurn:
                        child.changeVal(i, j, 'o')
                    else:
                        child.changeVal(i, j, 'x')
                
                    children.append(child)


        return children
    
    def connect4children(self, engineTurn: bool) -> set:
        children = set()


        for i in range(self.numCols):
            if self.board[0][i] == ' ':
                child = self.new_copy()
                child.dropPiece(i, engineTurn)
                children.add(child)




        return children
    
    def checkers_o_moves(self) -> set:
        s = set()
        
        
        return s
    
    
    def checkers_x_moves(self) -> set:
        s = set()
        
        return s
    
    def checkersChildren(self, engineTurn: bool) -> set:
        if engineTurn:
           return self.checkers_o_moves()
        return self.checkers_x_moves()
        
    
    def tictactoeEval(self):
        #unfinished game is 'neutral' in tic-tac-toe
        if not self.tictactoeGameComplete():
            return 0
        

        #Checking for horizonal win
        for i in range(self.numRows):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != ' ':
                if self.board[i][0] == 'o':
                    return 1
                else:
                    return -1
                

        #Checking for vertical win
        for i in range(self.numCols):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != ' ':
                if self.board[0][i] == 'o':
                    return 1
                else:
                    return -1
                
        
        #Checking for main diagonal win
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != ' ':
            if self.board[0][0] == 'o':
                return 1
            return -1
        
        if self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2] and self.board[2][0] != ' ':
            if self.board[2][0] == 'o':
                return 1
            return -1
        
        return 0
        
    def connect4Eval(self):
        '''
        maybe 1 point outer column per piece, 2, 3, then 4 for middle column, respectively
        1000 points for 4 in a row
        50 points per 3 in a row
        '''

        #Horizontal Win check
        for i in range(self.numCols - 3):
            for j in range(self.numRows):
                if self.board[j][i] != ' ' and (self.board[j][i] == self.board[j][i+1] == self.board[j][i+2] == self.board[j][i+3]):
                    return math.inf if self.board[j][i] == 'o' else -math.inf

        #Vertical Win check
        for i in range(self.numRows - 3):
            for j in range(self.numCols):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
                    return math.inf if self.board[i][j] == 'o' else -math.inf
                
        #Check for wins in '\' direction
        for i in range(self.numRows - 3):
            for j in range(self.numCols - 3):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
                    return math.inf if self.board[i][j] == 'o' else -math.inf

        #Check for wins in '/' direction
        for i in range(self.numRows - 1, 2, -1):
            for j in range(self.numCols - 3):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]):
                    return math.inf if self.board[i][j] == 'o' else -math.inf

        #If there's no win yet, then we have to do a different way of scoring
        score = 0
        score_decrements = {0: 1, 1: 2, 2: 3, 3: 4, 4: 3, 5: 2, 6: 1}
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == 'x':
                    score -= score_decrements[j]
                elif self.board[i][j] == 'o':
                    score += score_decrements[j]                   


        #Checking for 3 in a row:

        #Horizontal check
        for i in range(self.numCols - 2):
            for j in range(self.numRows):
                if self.board[j][i] != ' ' and (self.board[j][i] == self.board[j][i+1] == self.board[j][i+2]):
                    score = score + 50 if self.board[j][i] == 'o' else score - 50
        
        #Vertical check
        for i in range(self.numRows - 2):
            for j in range(self.numCols):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j] == self.board[i+2][j]):
                    score = score + 50 if self.board[i][j] == 'o' else score - 50

        # '\' direction
        for i in range(self.numRows - 2):
            for j in range(self.numCols - 2):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2]):
                    score = score + 50 if self.board[i][j] == 'o' else score - 50

        # '/' direction
        for i in range(self.numRows - 1, 1, -1):
            for j in range(self.numCols - 2):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2]):
                    score = score + 50 if self.board[i][j] == 'o' else score - 50

        return score

    def checkersEval(self):
        score = 0
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == ' ':
                    continue
                elif self.board[i][j] == 'o':
                    score += 3
                elif self.board[i][j] == 'O':
                    score += 5
                elif self.board[i][j] == 'x':
                    score -= 3
                else: #self.board[i][j] == 'X':
                    score -= 5

        
        return score

    #Engine maximizing, user minimizing
    def evalGame(self, game_no: int) -> int:
        if game_no == 1:
            return self.tictactoeEval() 
        elif game_no == 2:
            return self.connect4Eval()
        
        elif game_no == 3:
            return self.checkersEval()
        return 0
    
    #Returns True if the indicated game is complete, False otherwise
    def gameComplete(self, game_no):
        if game_no == 1:
            return self.tictactoeGameComplete()          
        elif game_no == 2:
            return self.connect4Complete()    
        
        elif game_no == 1:
            return self.checkersComplete()
        
        
        return True         
        
    def checkersComplete(self):
        o_left = False
        x_left = False
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == 'o' or self.board[i][j] == 'O':
                    o_left = True
                if self.board[i][j] == 'x' or self.board[i][j] == 'X':
                    x_left = True
                
                if o_left and x_left:
                    return False
                
        return True
        
    def connect4Complete(self):
        #Check for horizontal wins
        for i in range(self.numCols - 3):
            for j in range(self.numRows):
                if self.board[j][i] != ' ' and (self.board[j][i] == self.board[j][i+1] == self.board[j][i+2] == self.board[j][i+3]):
                    # - win, game over
                    return True


        #Check for vertical wins
        for i in range(self.numRows - 3):
            for j in range(self.numCols):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
                    # | win, game over
                    return True

        #Check for wins in '\' direction
        for i in range(self.numRows - 3):
            for j in range(self.numCols - 3):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
                    # \ win, game over
                    return True
                
        
        #Check for wins in '/' direction
        if True:
            for i in range(self.numRows - 1, 2, -1):
                for j in range(self.numCols - 3):
                    if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]):
                        # / win, game over
                        return True

            


        #If no win, check to see if top of the board is full
        for i in range(self.numCols):
            if self.board[0][i] == ' ':       
                return False
        
        #Board full, game over
        return True
    
    def tictactoeGameComplete(self):

        #Checking for 3 in a row

        #Checking for horizonal connections
        for i in range(self.numRows):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != ' ':
                return True
            
        #Checking for vertical connections
        for i in range(self.numCols):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != ' ':
                return True
        
        #Checking for main diagonal connection
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        
        #Checking for other diagonal connection
        if self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2] and self.board[2][0] != ' ':
            return True
        
        #Checking for full board
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == ' ':
                    return False
        
        #Board is full with no winner
        return True