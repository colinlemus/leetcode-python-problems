# Problem 11 - Two Sum II - Sorted

# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Example 1:
# Input: numbers = [1,2,4,6,10], target = 8
# Output: [1,3]
# Explanation: The numbers from 1 to 4 sum to 8. Thus the indices of 1 and 3 are returned.

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]

# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

# Solution Benchmark Analysis:
# Runtime: 0.3858 μs
# Memory Usage: 72 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# The function uses a two-pointer approach to find two elements in the numbers list that add up to the target value.
# The function initializes two pointers, left and right, at the beginning and end of the numbers list, respectively. It then loops until the two pointers meet in the middle. At each iteration of the loop, the function calculates the sum of the two elements at the current pointers.
# If the sum is equal to the target value, the function returns a list containing the indices of the two elements, incremented by 1 to make them 1-indexed.
# If the sum is less than the target value, the function moves the left pointer to the right to increase the sum.
# If the sum is greater than the target value, the function moves the right pointer to the left to decrease the sum.
# If no solution is found, the function returns an empty list.
# Overall, this function is an efficient and optimal solution to the Two Sum II - Input array is sorted problem, with a time complexity of O(n) and a space complexity of O(1), where n is the length of the numbers list.


def main(numbers, target):
    # Initialize two pointers at the beginning and end of the array
    left, right = 0, len(numbers) - 1

    # Loop until the two pointers meet
    while left < right:
        # Calculate the sum of the two elements at the current pointers
        sum = numbers[left] + numbers[right]

        # If the sum is equal to the target, return the indices of the two elements
        if sum == target:
            return [left + 1, right + 1]  # 1-indexed

        # If the sum is less than the target, move the left pointer to the right
        elif sum < target:
            left += 1

        # If the sum is greater than the target, move the right pointer to the left
        else:
            right -= 1

    # If no solution is found, return an empty list
    return []
