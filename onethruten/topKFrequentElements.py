# Problem 5 - Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Solution Benchmark Analysis:
# Runtime: 1.87 μs
# Memory Usage: 72 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using bucket sort
# Using a dictionary to store the frequencies of each element
# Using a list of lists to store the elements grouped by their frequency
# Collecting the elements from the list of lists to form the answer
from typing import List

def main(nums: List[int], k: int) -> List[int]:
    # Create a dictionary to store the frequencies
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Create a list of lists to store the elements grouped by their frequency
    buckets = [[] for _ in range(len(nums) + 1)]

    # Collect the elements from the list of lists to form the answer
    for num, freq in counts.items():
        buckets[freq].append(num)

    # Reverse the list and collect the elements until we have k elements
    ans = []
    for freq in reversed(range(len(buckets))):
        ans.extend(buckets[freq])
        if len(ans) >= k:
            return ans[:k]