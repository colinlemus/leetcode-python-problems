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
# Space complexity: O(n)

# Explanation:
# Using a hashmap to store the anagram groups
# Sorting the words and using the sorted word as the key
# If the sorted word is already in the hashmap, append the word to the list
# If not, create a new list with the word as the first element
from typing import List

def main(strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    return list(anagram_groups.values())