# Problem 14 - Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5

# Solution Benchmark Analysis:
# Runtime: 5.3106 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# This algorithm uses dynamic programming to find the amount of water that can be trapped after raining.
# The idea is to keep track of the maximum height seen so far from the left and right sides, and calculate the amount of water trapped at each position based on the minimum of the maximum heights seen so far and the height at that position.
# The algorithm calculates the maximum height seen so far from the left and right sides using two arrays, and then calculates the amount of trapped water at each position using these arrays.
# This algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array.


# Implementing the solution for trapping rain water problem
def main(height):
    n = len(height)
    if n == 0:
        return 0

    # Initialize arrays to keep track of the maximum height seen so far from the left and right sides
    left_max = [0] * n
    right_max = [0] * n
    trapped_water = 0

    # Calculate left_max
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Calculate right_max
    right_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Calculate trapped water
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    # Return the total amount of trapped water
    return trapped_water
