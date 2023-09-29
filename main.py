# File for holding the problems and solutions
# Benchmark CPU for every problem: I9-9900K
from typing import List
from utilities import display_benchmark_results
from onethruten.containsDuplicate import main as containsDuplicate
from onethruten.validAnagram import main as validAnagram
from onethruten.twoSum import main as twoSum
from onethruten.groupAnagrams import main as group_anagrams
from onethruten.topKFrequentElements import main as top_k_frequent
from onethruten.productOfArrayExceptSelf import main as productExceptSelf
from onethruten.validSudoku import main as validSudoku

# Problem 1 - Contains Duplicate
display_benchmark_results(
    "Contains Duplicate", containsDuplicate, "O(n)", "O(n)", [1, 2, 3, 1]
)

# Problem 2 - Valid Anagram
display_benchmark_results("Valid Anagram", validAnagram, "O(n)", "O(1)", "rat", "car")
display_benchmark_results(
    "Valid Anagram", validAnagram, "O(n)", "O(1)", "anagram", "nagaram"
)

# Problem 3 - Two Sum
display_benchmark_results("Two Sum", twoSum, "O(n)", "O(n)", [2, 7, 11, 15], 9)

# Problem 4 - Group Anagrams
display_benchmark_results(
    "Group Anagrams",
    group_anagrams,
    "O(n*klogk)",
    "O(n)",
    ["eat", "tea", "tan", "ate", "nat", "bat"],
)

# Problem 5 - Top K Frequent Elements
display_benchmark_results(
    "Top K Frequent Elements", top_k_frequent, "O(n)", "O(n)", [1, 1, 1, 2, 2, 3], 2
)

# Problem 6 - Product of Array Except Self
display_benchmark_results(
    "Product of Array Except Self", productExceptSelf, "O(n)", "O(1)", [1, 2, 3, 4]
)

# Problem 7 - Valid Sudoku
test_board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test_board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
display_benchmark_results("Valid Sudoku", validSudoku, "O(n^2)", "O(n^2)", test_board1)
display_benchmark_results("Valid Sudoku", validSudoku, "O(n^2)", "O(n^2)", test_board2)
