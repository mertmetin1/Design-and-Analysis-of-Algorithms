def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, col):
    # If all queens are placed
    if col >= len(board):
        return True
    
    # Consider this column and try placing this queen in all rows
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            
            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution, then backtrack
            board[i][col] = 0
    
    # If queen can not be placed in any row in this column
    return False

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def find_all_n_queens_solutions(n):
    board = [[0] * n for _ in range(n)]
    
    if not solve_n_queens(board, 0):
        print("No solution exists")
        return
    
    print("All solutions:")
    print_solution(board)

    count = 1
    while solve_n_queens(board, 0):
        print(f"Solution {count}:")
        print_solution(board)
        count += 1

# Example usage:
n = 10  # Board size
find_all_n_queens_solutions(n)
