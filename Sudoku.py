def solveSudoku(board):

    def isValid(row, col, num):
        for j in range(9):
            if board[row][j] == num:
                return False

        for i in range(9):
            if board[i][col] == num:
                return False

        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in "123456789":
                        if isValid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = "."
                    return False
        return True

    solve()


print("Enter Sudoku row by row (use . for empty):")

board = []
for i in range(9):
    row = input(f"Row {i+1}: ")
    board.append(list(row.strip()))

solveSudoku(board)

print("\nSolved Sudoku:")
for row in board:
    print(" ".join(row))
