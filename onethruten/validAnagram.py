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
# This algorithm checks if two input strings are anagrams of each other.
# The algorithm first checks if the two strings have the same length.
# The algorithm then uses a single hashmap to store the character frequencies of the first string.
# The algorithm increments the count for each character in the first string.
# The algorithm then decrements the count for each character in the second string.
# If a character is not present in the hashmap or its count is already 0, the strings are not anagrams.
# If the algorithm goes through both strings without returning False, the strings must be anagrams.
# This algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input strings.

# Visualization:
# {'a': 1}
# {'a': 1, 'n': 1}
# {'a': 2, 'n': 1}
# {'a': 2, 'n': 1, 'g': 1}
# {'a': 2, 'n': 1, 'g': 1, 'r': 1}
# {'a': 3, 'n': 1, 'g': 1, 'r': 1}
# {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
# {'a': 3, 'n': 0, 'g': 1, 'r': 1, 'm': 1}
# {'a': 2, 'n': 0, 'g': 1, 'r': 1, 'm': 1}
# {'a': 2, 'n': 0, 'g': 0, 'r': 1, 'm': 1}
# {'a': 1, 'n': 0, 'g': 0, 'r': 1, 'm': 1}
# {'a': 1, 'n': 0, 'g': 0, 'r': 0, 'm': 1}
# {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 1}
# {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}


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
