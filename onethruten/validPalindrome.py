# Problem 19 - Valid Palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: s = "race a car"
# Output: false

# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

# Solution Benchmark Analysis:
# Runtime: 2.2308 μs (valid) 0.9324 μs (invalid)
# Memory Usage: 24 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# This algorithm checks if an input string is a valid palindrome.
# The algorithm first converts the input string to lowercase and removes all non-alphanumeric characters.
# The algorithm then uses two pointers to compare characters from both ends of the string.
# If the characters at the two pointers are not equal, the string is not a valid palindrome.
# If the algorithm goes through the entire string without returning False, the string is a valid palindrome. # This algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.


def main(s: str) -> bool:
    # Convert string to lowercase and remove non-alphanumeric characters
    s = "".join(filter(str.isalnum, s.lower()))

    # Use two pointers to compare characters from both ends of the string
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
