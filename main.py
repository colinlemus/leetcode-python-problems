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
from onethruten.encodeDecodeStrings import main as encodeDecodeStrings
from onethruten.longestConsecutiveSequence import main as longestConsecutiveSequence
from onethruten.validPalindrome import main as validPalindrome


def displayOneThruTen():
    # Problem 1 - Contains Duplicate
    display_benchmark_results(
        "Contains Duplicate", containsDuplicate, "O(n)", "O(n)", [1, 2, 3, 1]
    )

    # Problem 2 - Valid Anagram
    display_benchmark_results(
        "Valid Anagram", validAnagram, "O(n)", "O(1)", "rat", "car"
    )
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
    display_benchmark_results(
        "Valid Sudoku", validSudoku, "O(n^2)", "O(n^2)", test_board1
    )
    display_benchmark_results(
        "Valid Sudoku", validSudoku, "O(n^2)", "O(n^2)", test_board2
    )

    # Problem 8 - Encode & Decode Strings
    display_benchmark_results(
        "Encode & Decode Strings", encodeDecodeStrings, "O(n)", "O(n)", "test"
    )

    # Problem 9 - Longest Consecutive Sequence
    display_benchmark_results(
        "Longest Consecutive Sequence",
        longestConsecutiveSequence,
        "O(n)",
        "O(n)",
        [100, 4, 200, 1, 3, 2],
    )

    # Problem 10 - Valid Palindrome
    display_benchmark_results(
        "Valid Palindrome",
        validPalindrome,
        "O(n)",
        "O(n)",
        "A man, a plan, a canal: Panama",
    )
    display_benchmark_results(
        "Valid Palindrome", validPalindrome, "O(n)", "O(n)", "race a car"
    )


from twothrutwenty.twoSumSorted import main as twoSumSorted
from twothrutwenty.threeSum import main as threeSum
from twothrutwenty.containerMostWater import main as containerMostWater


def displayTwoThruTwenty():
    # Problem 11 - Two Sum II - Sorted
    display_benchmark_results(
        "Two Sum II - Sorted", twoSumSorted, "O(n)", "O(1)", [2, 7, 11, 15], 9
    )

    # Problem 12 - 3Sum
    display_benchmark_results("3Sum", threeSum, "O(n^2)", "O(1)", [-1, 0, 1, 2, -1, -4])

    # Problem 13 - Container With Most Water
    display_benchmark_results(
        "Container With Most Water",
        containerMostWater,
        "O(n)",
        "O(1)",
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
    )


# Create a dictionary to map user input to functions
folder_functions = {
    1: displayOneThruTen,
    2: displayTwoThruTwenty,
}

while True:
    try:
        # Accept an integer input from the user
        print(
            "Enter a number relative to the folder of algorithms to run them. (ex: 1 == onethruten)"
        )
        user_input = int(input("Folder Number: "))

        # Check if the input is within the specified range (1-10)
        if user_input == 0:
            break
        elif user_input < 1 or user_input > 10:
            print("Please enter a number between 1 and 10.")
        else:
            # Get the corresponding function from the dictionary and call it
            folder_function = folder_functions.get(user_input)
            if folder_function:
                folder_function()
            else:
                print("No function defined for this folder.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
