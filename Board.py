class Board(object):
    def __init__(self, numRows: int, numCols: int):
        self.numRows = numRows
        self.numCols = numCols
        self.board = [  ]
        row = []
        for i in range(numCols):
            row.append(' ')
        for i in range(numRows):
            self.board.append(row[:])

    def __str__(self):
        s = ''

        for i in range(self.numRows):
            s += str(self.board[i]) + '\n'

        return s[:-1]

    def changeVal(self, row: int, col: int, newVal):
        self.board[row][col] = newVal

    def evalGame(self, game_no):

        return 