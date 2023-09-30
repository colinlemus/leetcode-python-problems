# Problem 19 - Sliding Window Maximum

# Given an array of integers nums and an integer k, return the maximum sliding window of size k in nums.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

# Solution Benchmark Analysis:
# Runtime: 0.9973 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(k)

# Explanation:
# This algorithm finds the maximum value in each sliding window of size k in an input array.
# The algorithm uses a deque to store the indices of the elements in the current window.
# The algorithm iterates over the array and removes elements from the front of the deque that are outside the current window.
# The algorithm also removes elements from the back of the deque that are smaller than the current element.
# The algorithm adds the index of the current element to the back of the deque.
# If the current index is greater than or equal to k - 1, the algorithm appends the maximum value in the current window to the max_values list.
# Finally, the algorithm returns the max_values list.
# This algorithm has a time complexity of O(n) and a space complexity of O(k), where k is the size of the sliding window.

from collections import deque


def main(nums, k):
    # Initialize variables
    max_values = []
    # Create an empty deque to store the indices of the elements in the current window
    dq = deque()

    for i, n in enumerate(nums):
        # Remove elements out of the window from the front
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < n:
            dq.pop()

        dq.append(i)

        # The front of the deque is the maximum element for the current window
        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values
