# Problem 1 - Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# Solution Benchmark Analysis:
# Runtime: 0.33 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using a set to store the values and checking if the value is already in the set
# Sets can only contain unique values, so if the value is already in the set, we know it's a duplicate


def main(nums):
    # Create a set to hold the values
    values = set()

    for num in nums:
        # Check if num is already in the set
        if num in values:
            return True  # Return True immediately if a duplicate is found
        values.add(num)  # Otherwise, add the num to the set
    return False  # Return False if no duplicates are found


# Solution 2 - Not using Sets

# Solution 2 Benchmark Analysis:
# Runtime: 0.46 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)


# Explanation:
# The function checks for duplicate elements in an array and returns True if any are found, otherwise False.
# It uses a dictionary for efficient lookups.


def solution_2(nums):
    # Create a dictionary to store the frequency of each element in the array
    freq = {}

    # Iterate over the array and update the frequency of each element in the dictionary
    for num in nums:
        # If the element is already in the dictionary, increment its frequency by 1
        if num in freq:
            # Increment the frequency of the element by 1
            return True

        # If the element is not in the dictionary, add it to the dictionary with a frequency of 1
        freq[num] = 1

    # Iterate over the dictionary and check if any element has a frequency greater than 1
    return False


import unittest


class TestContainsDuplicate(unittest.TestCase):
    def run_solution_tests(self, solution):
        self.assertFalse(solution([]), "Failed on empty list")
        self.assertFalse(solution([1, 2, 3, 4, 5]), "Failed on no duplicates")
        self.assertTrue(solution([1, 2, 3, 4, 4]), "Failed on with duplicates")
        self.assertTrue(solution(list(range(10000)) + [9999]), "Failed on large list")
        self.assertTrue(solution([-1, -2, -3, -1]), "Failed on negative numbers")
        self.assertFalse(solution(list(range(-10000, 10000))), "Failed on large range")
        self.assertTrue(solution([1.1, 2.2, 3.3, 1.1]), "Failed on non-integer values")
        self.assertTrue(solution([1, 2, 3, 1, 2, 3]), "Failed on repeating patterns")
        self.assertFalse(solution([1]), "Failed on single element")
        self.assertTrue(solution([1, 1, 1, 1]), "Failed on all duplicates")
        self.assertTrue(solution([True, False, True]), "Failed on list of booleans")

    def test_solution_1(self):
        self.run_solution_tests(main)

    def test_solution_2(self):
        self.run_solution_tests(solution_2)


if __name__ == "__main__":
    unittest.main()
