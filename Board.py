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

    def new_copy(self):
        new = Board(self.numRows, self.numCols)
        new.setBoard(self.board)
        return new


    def __str__(self):
        s = ''

        for i in range(self.numRows):
            s += str(self.board[i]) + '\n'

        return s

    def changeVal(self, row: int, col: int, newVal):
        self.board[row][col] = newVal

    def getVal(self, row: int, col: int, newVal):
        return self.board[row][col]


    def getChildren(self, game_no: int, engineTurn: bool) -> list:
        if game_no == 1:
            return self.tictactoeChildren(engineTurn) 


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
    
    def tictactoeEval(self):
        return -1

    def evalGame(self, game_no: int) -> int:
        if game_no == 1:
            return self.tictactoeEval() 
        
    def gameComplete(self, game_no):
        if game_no == 1:
            return self.tictactoeGameComplete()
        
    def tictactoeGameComplete(self):

        #Checking for 3 in a row
        for i in range(self.numRows):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                return True
            
        for i in range(self.numCols):
            if self.board[0][i] == self.board[1][i] and self.board[0][0] == self.board[2][i]:
                return True
        
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return True
        
        if self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2]:
            return True
        
        #Checking for full board
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] == ' ':
                    return False
        
        #Board is full with no winner
        return True