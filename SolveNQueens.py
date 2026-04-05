def solveNQueens(n):
    result = []
    board = [["."] * n for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()
    def backtrack(row):
        if row == n:
            temp = ["".join(r) for r in board]
            result.append(temp)
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row +  col) in diag2:
                continue
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    backtrack(0)
    return result
n = int(input("Enter the value of n: "))
solutions = solveNQueens(n)
print("no of solutions: ", len(solutions))
print("solutions: ")
for sol in solutions:
    for row in sol:
        print(row)
    print()
