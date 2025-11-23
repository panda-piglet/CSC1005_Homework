#检查一个位置能不能摆放皇后
def check_place(row,col):
    global chessboard
    for board_row in range(row):
        #访问棋盘的行数索引获得的是列
        if chessboard[board_row] == col:
            return False
        if abs(board_row - row) == abs(chessboard[board_row] - col):
            return False
    return True

#对每一行摆放一个皇后
def place_queen(row):
    global chessboard,solutions
    if row == 8:
        solutions += 1
        return

    for col in range(8):
        if check_place(row,col) == True:
            chessboard[row] = col
            place_queen(row + 1)

chessboard=[-1 for i in range(8)]
solutions = 0
row = 0
place_queen(row)
print(solutions)

    
