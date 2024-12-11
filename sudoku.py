def is_valid_move(grid, row, col, num):
    """Check if placing num at grid[row][col] is valid."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num  # Make a tentative move

                        if solve_sudoku(grid):  # Recursively try to solve the rest
                            return True

                        grid[row][col] = 0  # Undo the move if it doesn't lead to a solution

                return False  # Trigger backtracking if no number works

    return True  # Return True if the grid is completely solved

def print_grid(grid):
    """Print the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

if __name__ == "__main__":
    # Example unsolved Sudoku grid (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Unsolved Sudoku Puzzle:")
    print_grid(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_grid(puzzle)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")
