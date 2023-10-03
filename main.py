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
    # Start of Array & Hashing problems
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
    display_benchmark_results("Valid Sudoku", validSudoku, "O(1)", "O(1)", test_board1)
    display_benchmark_results("Valid Sudoku", validSudoku, "O(1)", "O(1)", test_board2)

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

    # Start of Two Pointer problems
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


from tenthrutwenty.twoSumSorted import main as twoSumSorted
from tenthrutwenty.threeSum import main as threeSum
from tenthrutwenty.containerMostWater import main as containerMostWater
from tenthrutwenty.trappingRainWater import main as trappingRainWater
from tenthrutwenty.bestTimeBuySellStock import main as bestTimeBuySellStock
from tenthrutwenty.longestSubstringNoRepeatCharacters import (
    main as longestSubstringWithoutRepeatingCharacters,
)
from tenthrutwenty.longestRepeatingCharacterReplacement import (
    main as longestRepeatingCharacterReplacement,
)
from tenthrutwenty.minimumWindowSubstring import main as minimumWindowSubstring
from tenthrutwenty.slidingWindowMaximum import main as slidingWindowMaximum


def displayTenThruTwenty():
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

    # Problem 14 - Trapping Rain Water
    display_benchmark_results(
        "Trapping Rain Water",
        trappingRainWater,
        "O(n)",
        "O(1)",
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    )

    # Start of Sliding Window problems
    # Problem 15 - Best Time to Buy and Sell Stock
    display_benchmark_results(
        "Best Time to Buy and Sell Stock",
        bestTimeBuySellStock,
        "O(n)",
        "O(1)",
        [7, 1, 5, 3, 6, 4],
    )

    # Problem 16 - Longest Substring Without Repeating Characters
    display_benchmark_results(
        "Longest Substring Without Repeating Characters",
        longestSubstringWithoutRepeatingCharacters,
        "O(n)",
        "O(min(n, m))",
        "abcabcbb",
    )

    # Problem 17 - Longest Repeating Character Replacement
    display_benchmark_results(
        "Longest Repeating Character Replacement",
        longestRepeatingCharacterReplacement,
        "O(n)",
        "O(1)",
        "ABAB",
        2,
    )

    # Problem 18 - Minimum Window Substring
    display_benchmark_results(
        "Minimum Window Substring",
        minimumWindowSubstring,
        "O(n)",
        "O(m)",
        "ADOBECODEBANC",
        "ABC",
    )

    # Problem 19 - Sliding Window Maximum
    display_benchmark_results(
        "Sliding Window Maximum",
        slidingWindowMaximum,
        "O(n)",
        "O(k)",
        [1, 3, -1, -3, 5, 3, 6, 7],
        3,
    )


from twentythruthirty.validParentheses import main as validParentheses
from twentythruthirty.minimumAddMakeParenthesesValid import (
    main as minimumAddMakeParenthesesValid,
)


def displayTwentyThruThirty():
    # Start of Stack problems
    # Problem 20 - Valid Parentheses
    display_benchmark_results(
        "Valid Parentheses", validParentheses, "O(n)", "O(n)", "{[]}"
    )

    # Problem 21 - Minimum Add to Make Parentheses Valid
    display_benchmark_results(
        "Minimum Add to Make Parentheses Valid",
        minimumAddMakeParenthesesValid,
        "O(n)",
        "O(n)",
        "())",
    )

    # Problem 22 - Evaluate Reverse Polish Notation

    # Problem 23 - Generate Parentheses

    # Problem 24 - Daily Temperatures

    # Problem 25 - Car Fleet

    # Problem 26 - Largest Rectangle in Histogram

    # Start of Binary Search problems
    # Problem 27 - Binary Search

    # Problem 28 - Search a 2D Matrix

    # Problem 29 - Koko Eating Bananas

    return


def displayThirtyThruForty():
    # Problem 30 - Find Minimum in Rotated Sorted Array

    # Problem 31 - Search in Rotated Sorted Array

    # Problem 32 - Time Based Key-Value Store

    # Problem 33 - Median of Two Sorted Arrays

    # Start of Linked List problems

    return


# Create a dictionary to map user input to functions
folder_functions = {
    1: displayOneThruTen,
    2: displayTenThruTwenty,
    3: displayTwentyThruThirty,
    4: displayThirtyThruForty,
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
