# File for holding the problems and solutions
import time
import sys
import timeit

# Benchmarking function
def benchmark(function, *args):
    """
    Benchmark the given function with the provided arguments.
    
    Parameters:
    - function: The function to be benchmarked.
    - *args: Arguments to pass to the function.
    
    Returns:
    - result: Result of the function execution.
    - elapsed_time: Time taken for execution in seconds.
    - memory_used: Approximate memory used by the result in bytes.
    """
    
    # Wrap the function call in a lambda to pass to timeit
    func_lambda = lambda: function(*args)
    
    # Use timeit to get the average time over multiple runs
    # Here, we'll run the function 1000 times by default
    num_runs = 1000
    total_time = timeit.timeit(func_lambda, number=num_runs)
    average_time = total_time / num_runs
    
    # Execute the function once to get the result and memory usage
    result = function(*args)
    memory_used = sys.getsizeof(result)
    
    return result, average_time, memory_used

def display_benchmark_results(problem_name, function, time_complexity, space_complexity, *args):
    """
    Benchmark the given function and display the results in a structured format.
    
    Parameters:
    - problem_name: The name of the problem or task being benchmarked.
    - function: The function to be benchmarked.
    - time_complexity: Time complexity of the algorithm (as a string).
    - space_complexity: Space complexity of the algorithm (as a string).
    - *args: Arguments to pass to the function.
    """
    result, elapsed_time, memory_used = benchmark(function, *args)
    
    # Print the results in a structured format
    print(f"Problem: {problem_name}")
    print(f"Inputs: {', '.join(map(str, args))}")
    print(f"Result: {result}")
    print(f"Time Complexity: {time_complexity}")
    print(f"Space Complexity: {space_complexity}")
    print(f"Elapsed Time: {elapsed_time:.2e} seconds")
    print(f"Memory Used: {memory_used} bytes")
    print("-" * 40)

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

# Solution
# Runtime: 124 ms, faster than 99.23% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 21.5 MB, less than 5.04% of Python3 online submissions for Contains Duplicate.
# Time complexity: O(n)
# Space complexity: O(n)

def containsDuplicate(nums):
    # Create a set to hold the values
    values = set()
    for num in nums:
        if num in values:
            return True
        else:
            values.add(num)
    return False

display_benchmark_results("Contains Duplicate", containsDuplicate, "O(n)", "O(n)", [1,2,3,1])

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

# Solution

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
display_benchmark_results("Valid Anagram", isAnagram, "O(n)", "O(1)", "anagram", "nagaram")

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

# Solution
# Runtime: 44 ms, faster than 99.34% of Python3 online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 55.58% of Python3 online submissions for Two Sum.
# Time complexity: O(n)
# Space complexity: O(n)

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

display_benchmark_results("Two Sum", twoSum, "O(n)", "O(n)", [2,7,11,15], 9)