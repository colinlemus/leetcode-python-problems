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
# Using a dictionary to store the values
# Checking if the complement exists in the dictionary
# If it does, return the indices
# If not, add the value to the dictionary


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
