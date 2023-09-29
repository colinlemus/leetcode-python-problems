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
# Runtime: 1.76 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Using a hashmap to store the character frequencies of 's'
# Then decrementing the count for each character in 't'
# If the count is already 0 or the character is not present, the strings are not anagrams


def main(s, t):
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