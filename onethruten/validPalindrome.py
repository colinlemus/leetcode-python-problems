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
# Using two pointers to compare characters from both ends of the string
# Convert string to lowercase and remove non-alphanumeric characters
# If the characters don't match, the string is not a palindrome
# If the characters match, increment the left pointer and decrement the right pointer
# Return True if the string is a palindrome
# Return False if the string is not a palindrome

def main(s: str) -> bool:
    # Convert string to lowercase and remove non-alphanumeric characters
    s = ''.join(filter(str.isalnum, s.lower()))
    
    # Use two pointers to compare characters from both ends of the string
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True