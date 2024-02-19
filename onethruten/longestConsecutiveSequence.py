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


import unittest


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(main([100, 4, 200, 1, 3, 2]), 4)

    def test_extended_sequence(self):
        self.assertEqual(main([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_empty_array(self):
        self.assertEqual(main([]), 0)

    def test_single_element(self):
        self.assertEqual(main([10]), 1)

    def test_duplicates(self):
        self.assertEqual(main([1, 2, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(main([-3, -2, -1, 0, 1]), 5)

    def test_non_consecutive_array(self):
        self.assertEqual(main([10, 20, 30]), 1)

    def test_large_array_with_one_sequence(self):
        self.assertEqual(main(list(range(-1000, 1001))), 2001)

    def test_mixed_numbers(self):
        self.assertEqual(main([-2, -3, 7, 5, 0, 1, 3, 4, 6]), 5)


if __name__ == "__main__":
    unittest.main()
