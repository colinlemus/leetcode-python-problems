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
# Runtime: 2.36 μs
# Memory Usage: 88 byes
# Time complexity: O(n*klogk)
# Space complexity: O(n*k)

# Explanation:
# This algorithm groups the input list of strings into anagrams.
# The algorithm sorts each string in the input list and uses the sorted string as the key in a hashmap.
# If two strings are anagrams, they will have the same sorted string, so the algorithm groups them together in the same list in the hashmap.
# The algorithm returns the values of the hashmap as a list of lists, where each inner list contains the anagram group.
# This algorithm has a time complexity of O(n*klogk) and a space complexity of O(n*k), where n is the length of the input list and k is the maximum length of a string in the input list.

from collections import defaultdict
from typing import List


def main(strs: List[str]) -> List[List[str]]:
    # Create a hashmap to store the anagram groups
    anagram_groups = defaultdict(list)

    for word in strs:
        # Sort the word to use as the key in the hashmap
        sorted_word = "".join(sorted(word))
        # Add the word to the anagram group
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())
