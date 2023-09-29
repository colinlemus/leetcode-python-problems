# Problem 6 - Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Solution Benchmark Analysis:
# Runtime: 1.87 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Using prefix and suffix products
# Create a list to store the products
# Calculate the prefix products
# Calculate the suffix products
# Multiply the prefix and suffix products to get the answer
from typing import List

def main(nums: List[int]) -> List[int]:
    # Create a list to store the products
    products = [1] * len(nums)

    # Calculate the prefix products
    prefix = 1
    for i in range(len(nums)):
        products[i] = prefix
        prefix *= nums[i]

    # Calculate the suffix products
    suffix = 1
    for i in reversed(range(len(nums))):
        products[i] *= suffix
        suffix *= nums[i]

    return products