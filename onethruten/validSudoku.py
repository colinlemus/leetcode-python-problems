# Problem 7 - Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false

# Constraints:
#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit or '.'.

# Solution Benchmark Analysis:
# Runtime: 18 μs (valid) 5 μs (invalid)
# Memory Usage: 28 bytes (valid) 24 bytes (invalid)
# Time complexity: O(n^2)
# Space complexity: O(n^2)

# Explanation:
# Using sets to store the values in each row, column, and box
# Checking if the value is already in the set
# If it is, the board is not valid
# If not, add the value to the set
# Return True if the board is valid
# Return False if the board is not valid


def main(board):
    # Create sets to store the values in each row, column, and box
    rows, cols, boxes = (
        [set() for _ in range(9)],
        [set() for _ in range(9)],
        [set() for _ in range(9)],
    )

    # Iterate x axis of the board
    for i in range(9):
        # Iterate y axis of the board
        for j in range(9):
            # Check if the value is already in the set
            num = board[i][j]
            if num == ".":
                continue

            # If it is, the board is not valid
            box_idx = (i // 3) * 3 + j // 3

            # Check if the value is already in the set
            if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_idx]):
                return False

            # If not, add the value to the set
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)

    return True
