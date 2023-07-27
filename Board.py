import copy

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
    
    def getBoard(self):
        return self.board

    def setBoard(self, otherBoard):
        self.board = [row[:] for row in otherBoard]

    def hash(self) -> int:
        s = ""
        for i in range(self.numRows):
            s += ''.join([item for item in self.board[i]])
            s += "\n"

        return hash(s)

    def new_copy(self):
        new = Board(self.numRows, self.numCols)
        new.setBoard(self.board)
        return new

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

    def tictactoeChildren(self, engineTurn: bool) -> set: 
        children = set()

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
                
                    children.add(child)


        return children
    
    #NEED TO IMPLEMENT
    def connect4children(self, engineTurn: bool) -> set:
        children = set()


        for i in range(self.numCols):
            if self.board[0][i] == ' ':
                child = self.new_copy()
                child.dropPiece(i, engineTurn)
                children.add(child)




        return children
    
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
        
    #NEED TO IMPLEMENT
    def connect4Eval(self):
        print("connect4Eval need to implement")
        return 0

    #Engine maximizing, user minimizing
    def evalGame(self, game_no: int) -> int:
        if game_no == 1:
            return self.tictactoeEval() 
        
        return 0
    
    def gameComplete(self, game_no):
        if game_no == 1:
            return self.tictactoeGameComplete()          
        elif game_no == 2:
            return self.connect4Complete()            
        
    #NEED TO IMPLEMENT
    def connect4Complete(self):
        #Check for horizontal wins
        for i in range(self.numCols - 3):
            for j in range(self.numRows):
                if self.board[j][i] != ' ' and (self.board[j][i] == self.board[j][i+1] == self.board[j][i+2] == self.board[j][i+3]):
                    print(" - win, game over")
                    return True


        #Check for vertical wins
        for i in range(self.numRows - 3):
            for j in range(self.numCols):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
                    print(" | win, game over")
                    return True

        #Check for wins in '\' direction
        for i in range(self.numRows - 3):
            for j in range(self.numCols - 3):
                if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
                    print(" \ win, game over")
                    return True
                
        
        #Check for wins in '/' direction
        if True:
            for i in range(self.numRows - 1, 2, -1):
                for j in range(self.numCols - 3):
                    if self.board[i][j] != ' ' and (self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]):
                        print(" / win, game over")
                        return True

            


        #If no win, check to see if top of the board is full
        for i in range(self.numCols):
            if self.board[0][i] == ' ':       
                return False
        
        print("Board full, game over")
        return True
    
    def tictactoeGameComplete(self):

        #Checking for 3 in a row

        #Checking for horizonal connections
        for i in range(self.numRows):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != ' ':
                #print("Game complete 0")
                return True
            
        #Checking for vertical connections
        for i in range(self.numCols):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != ' ':
                #print("Game complete 1")
                return True
        
        #Checking for main diagonal connection
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        
        #Checking for other diagonal connection
        if self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2] and self.board[2][0] != ' ':
            #print("Game complete 2")
            return True
        
        #Checking for full board
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == ' ':
                    return False
        
        #Board is full with no winner
        return True