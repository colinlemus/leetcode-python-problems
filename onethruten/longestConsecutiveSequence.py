# Problem 9 - Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# Solution Benchmark Analysis:
# Runtime: 0.99 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# This algorithm finds the length of the longest consecutive sequence in an input array of integers.
# The algorithm first checks if the input array is empty, and then converts the input array into a set for quick lookups.
# The algorithm then iterates over the set and checks if each number is the start of a sequence.
# If a number is the start of a sequence, the algorithm checks for consecutive numbers in the positive direction and updates the maximum length seen so far.
# The algorithm returns the maximum length of a consecutive sequence.
# This algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array.


def main(nums):
    if not nums:
        return 0

    # Convert the input array into a set for quick lookups
    num_set = set(nums)
    max_length = 0

    # Iterate over the set
    for num in num_set:
        # Check if the number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Check for consecutive numbers in the positive direction
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
