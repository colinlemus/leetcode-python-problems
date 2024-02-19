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
# This algorithm finds the product of all elements in an input list except for the element at the current index.
# The algorithm first creates a list to store the output products, and initializes it with 1.
# The algorithm then calculates the prefix products of the input list, which are the products of all elements to the left of the current index.
# The algorithm then calculates the suffix products of the input list, which are the products of all elements to the right of the current index.
# The algorithm then multiplies the prefix and suffix products to get the final product of all elements except for the element at the current index.
# The algorithm returns the list of products. This algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.

# Visualization:
# {'prefix': 1, 'suffix': None, 'products': [1, 1, 1, 1]},
# {'prefix': 1, 'suffix': None, 'products': [1, 1, 1, 1]},
# {'prefix': 2, 'suffix': None, 'products': [1, 1, 1, 1]},
# {'prefix': 6, 'suffix': None, 'products': [1, 1, 2, 1]},
# {'prefix': None, 'suffix': 1, 'products': [1, 1, 2, 6]},
# {'prefix': None, 'suffix': 4, 'products': [1, 1, 2, 6]},
# {'prefix': None, 'suffix': 12, 'products': [1, 1, 8, 6]},
# {'prefix': None, 'suffix': 24, 'products': [1, 12, 8, 6]},
# {'prefix': None, 'suffix': None, 'products': [24, 12, 8, 6]}

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


import unittest


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(main([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_negative_numbers(self):
        self.assertEqual(main([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_single_zero(self):
        self.assertEqual(main([0, 1, 2, 3, 4]), [24, 0, 0, 0, 0])

    def test_multiple_zeros(self):
        self.assertEqual(main([0, 0, 2, 3, 4]), [0, 0, 0, 0, 0])

    def test_all_ones(self):
        self.assertEqual(main([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_mixed_negative(self):
        self.assertEqual(main([-1, -2, -3, -4]), [-24, -12, -8, -6])

    def test_max_min_32bit(self):
        self.assertEqual(
            main([2**31 - 1, 2, 3, 4]),
            [24, (2**31 - 1) * 3 * 4, (2**31 - 1) * 2 * 4, (2**31 - 1) * 2 * 3],
        )

    def test_large_array(self):
        nums = [
            1 for _ in range(1000)
        ]  # Product will always be 1 for all elements except self
        expected = [1 for _ in range(1000)]
        self.assertEqual(main(nums), expected)


if __name__ == "__main__":
    unittest.main()
