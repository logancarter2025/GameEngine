from Board import *
row = int(input("Enter number of rows: ").strip())
col = int(input("Enter number of cols: ").strip())
b1 = Board(row, col)
b1.changeVal(1, 1, 'X')
print(b1)