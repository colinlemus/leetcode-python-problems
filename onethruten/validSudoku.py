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
# Runtime: 18.12 μs
# Memory Usage: 28 bytes
# Time complexity: O(1)
# Space complexity: O(1)

# Explanation:
# This algorithm checks if a given 9x9 Sudoku board is valid.
# The algorithm first creates three sets to store the values in each row, column, and box of the board.
# The algorithm then iterates over the board and checks if each value is already in the corresponding set for its row, column, and box.
# If a value is already in one of the sets, the board is not valid.
# If a value is not in any of the sets, the algorithm adds the value to the corresponding sets.
# If the algorithm goes through the entire board without returning False, the board is valid.
# This algorithm has a time complexity of O(1) and a space complexity of O(1), because the size of the board is fixed.


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
