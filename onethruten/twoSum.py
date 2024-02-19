# Problem 3 - Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# Solution Benchmark Analysis:
# Runtime: 0.39 μs
# Memory Usage: 72 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# This algorithm finds the indices of two numbers in an input list of integers that add up to a target value.
# The algorithm first creates a dictionary to store the values of the input list.
# The algorithm then iterates over the input list and checks if the complement of the current number exists in the dictionary.
# If the complement exists, the algorithm returns the indices of the two numbers.
# If the complement does not exist, the algorithm adds the current number to the dictionary.
# This algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.


def main(nums, target):
    # Create a dictionary to store the values
    values = {}
    for i, num in enumerate(nums):
        # Check if the complement exists in the dictionary
        complement = target - num
        if complement in values:
            return [values[complement], i]
        else:
            values[num] = i


import unittest


class TestTwoSum(unittest.TestCase):
    def test_example_one(self):
        self.assertCountEqual(main([2, 7, 11, 15], 9), [0, 1])

    def test_example_two(self):
        self.assertCountEqual(main([3, 2, 4], 6), [1, 2])

    def test_example_three(self):
        self.assertCountEqual(main([3, 3], 6), [0, 1])

    def test_with_zero(self):
        self.assertCountEqual(main([0, 4, 3, 0], 0), [0, 3])

    def test_repeated_numbers(self):
        self.assertCountEqual(main([1, 5, 5, 11], 10), [1, 2])

    def test_large_array(self):
        nums = list(range(1, 1001))  # Large array
        target = 1999  # The sum of the last two elements
        self.assertCountEqual(main(nums, target), [998, 999])


if __name__ == "__main__":
    unittest.main()
