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
# Runtime: 0.3347 μs
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
        if num in values:
            return True
        else:
            values.add(num)
    return False
