# Problem 13 - Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# Solution Benchmark Analysis:
# Runtime: 2.12 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# This algorithm uses a two-pointer approach to find the maximum area of the container.
# The idea is to start with the widest container and move the pointers towards each other to find a container with a greater area.
# The algorithm calculates the area of the container formed by the two lines at the current pointers, updates the max_area variable if necessary, and moves the pointers towards each other based on the height of the lines.
# This algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the length of the height array.


def main(height):
    # Initialize two pointers, left and right, at the beginning and end of the height array, respectively
    left, right = 0, len(height) - 1

    # Initialize a variable max_area to 0
    max_area = 0

    # Loop until the two pointers meet
    while left < right:
        # Calculate the area of the container formed by the two lines at left and right
        area = min(height[left], height[right]) * (right - left)

        # Update max_area to be the maximum of max_area and the calculated area
        max_area = max(max_area, area)

        # If the height of the line at left is less than the height of the line at right, move left to the right
        if height[left] < height[right]:
            left += 1

        # Otherwise, move right to the left
        else:
            right -= 1
    # Return max_area
    return max_area
