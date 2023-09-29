# File for holding the problems and solutions
# Benchmark CPU for every problem: I9-9900K
from typing import List
import sys
import timeit


def benchmark(function, *args, num_runs=1000):
    """
    Benchmark the given function with the provided arguments.

    Parameters:
    - function: The function to be benchmarked.
    - *args: Arguments to pass to the function.
    - num_runs: Number of times to run the function for benchmarking.

    Returns:
    - result: Result of the function execution.
    - elapsed_time: Time taken for execution in seconds.
    - memory_used: Approximate memory used by the result in bytes.
    """

    # Wrap the function call in a lambda to pass to timeit
    func_lambda = lambda: function(*args)

    # Use timeit to get the average time over multiple runs
    total_time = timeit.timeit(func_lambda, number=num_runs)
    average_time = total_time / num_runs

    # Execute the function once to get the result and memory usage
    result = function(*args)
    memory_used = sys.getsizeof(result)

    return result, average_time, memory_used


def display_benchmark_results(
    problem_name, function, time_complexity, space_complexity, *args
):
    result, elapsed_time, memory_used = benchmark(function, *args)
    elapsed_time_us = elapsed_time * 1000 * 1000  # Convert to microseconds for better precision
    
    header = f"📋 Problem: {problem_name}"
    inputs = f"🔠 Inputs: {', '.join(map(str, args))}"
    output = f"🎯 Result: {result}"
    
    complexities = f"🛠 Time: {time_complexity} | Space: {space_complexity}"
    metrics = f"⏱ Elapsed: {elapsed_time_us:.4f} μs | 📦 Memory: {memory_used} bytes"
    
    print(f"{header}\n{inputs}\n{output}\n{complexities}\n{metrics}")
    print("─" * 40)


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
# Runtime: 0.3779 ms
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using a set to store the values and checking if the value is already in the set
# Sets can only contain unique values, so if the value is already in the set, we know it's a duplicate

def containsDuplicate(nums):
    # Create a set to hold the values
    values = set()
    for num in nums:
        if num in values:
            return True
        else:
            values.add(num)
    return False


display_benchmark_results(
    "Contains Duplicate", containsDuplicate, "O(n)", "O(n)", [1, 2, 3, 1]
)

# Problem 2 - Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# Solution Benchmark Analysis:
# Runtime: 1.76 ms
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Using a hashmap to store the character frequencies of 's'
# Then decrementing the count for each character in 't'
# If the count is already 0 or the character is not present, the strings are not anagrams

def isAnagram(s, t):
    # Initial length check
    if len(s) != len(t):
        return False

    # Single hashmap to store character frequencies
    characterCount = {}

    # Increment count for each character in 's'
    for char in s:
        characterCount[char] = characterCount.get(char, 0) + 1

    # Decrement count for each character in 't'
    for char in t:
        # If character is not present or its count is already 0, strings are not anagrams
        if char not in characterCount or characterCount[char] == 0:
            return False
        characterCount[char] -= 1

    # If we've gone through both strings without returning False, they must be anagrams
    return True


display_benchmark_results("Valid Anagram", isAnagram, "O(n)", "O(1)", "rat", "car")
display_benchmark_results(
    "Valid Anagram", isAnagram, "O(n)", "O(1)", "anagram", "nagaram"
)

# Problem 3 - Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# Solution Benchmark Analysis:
# Runtime: 0.39 ms
# Memory Usage: 72 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using a dictionary to store the values
# Checking if the complement exists in the dictionary
# If it does, return the indices
# If not, add the value to the dictionary

def twoSum(nums, target):
    # Create a dictionary to store the values
    values = {}
    for i, num in enumerate(nums):
        # Check if the complement exists in the dictionary
        complement = target - num
        if complement in values:
            return [values[complement], i]
        else:
            values[num] = i


display_benchmark_results("Two Sum", twoSum, "O(n)", "O(n)", [2, 7, 11, 15], 9)

# Problem 4 - Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

# Solution Benchmark Analysis:
# Runtime: 2.36 ms
# Memory Usage: 88 byes
# Time complexity: O(n*klogk)
# Space complexity: O(n)

# Explanation:
# Using a hashmap to store the anagram groups
# Sorting the words and using the sorted word as the key
# If the sorted word is already in the hashmap, append the word to the list
# If not, create a new list with the word as the first element


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    return list(anagram_groups.values())


display_benchmark_results(
    "Group Anagrams",
    group_anagrams,
    "O(n*klogk)",
    "O(n)",
    ["eat", "tea", "tan", "ate", "nat", "bat"],
)

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
# Runtime: 1.87 ms
# Memory Usage: 72 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using bucket sort
# Using a dictionary to store the frequencies of each element
# Using a list of lists to store the elements grouped by their frequency
# Collecting the elements from the list of lists to form the answer

def top_k_frequent(nums: List[int], k: int) -> List[int]:
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

display_benchmark_results("Top K Frequent Elements", top_k_frequent, "O(n)", "O(n)", [1,1,1,2,2,3], 2)

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
# Runtime: 1.87 ms
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Using prefix and suffix products
# Create a list to store the products
# Calculate the prefix products
# Calculate the suffix products
# Multiply the prefix and suffix products to get the answer

def productExceptSelf(nums: List[int]) -> List[int]:
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

display_benchmark_results("Product of Array Except Self", productExceptSelf, "O(n)", "O(1)", [1,2,3,4])