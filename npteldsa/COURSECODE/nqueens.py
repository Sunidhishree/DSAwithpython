board = []
solutions = []
n = int(input("Enter number of queens: "))

def place(board, j):
    board.append(j)

def available(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def queen(n, row, board):
    for j in range(n):
        if available(board, row, j, n):
            place(board, j)
            if row == n - 1:
                solutions.append(board[:])
            else:
                queen(n, row + 1, board)
            board.pop()

def print_solutions(solutions, n):
    for sol in solutions:
        for i in range(n):
            row = ["."] * n
            row[sol[i]] = "Q"
            print(" ".join(row))
        print("\n")

queen(n, 0, board)
print_solutions(solutions, n)
