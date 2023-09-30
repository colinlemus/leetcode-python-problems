# Problem 16 - Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3

# Example 2:
# Input: s = "bbbbb"
# Output: 1

# Example 3:
# Input: s = "pwwkew"
# Output: 3

# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

# Solution Benchmark Analysis:
# Runtime: 2.8692 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(min(n, m))

# Explanation:
# This algorithm finds the length of the longest substring without repeating characters in an input string.
# The algorithm uses two pointers, left and right, to define a sliding window that contains a substring without repeating characters.
# The algorithm uses a set to store the unique characters in the current substring.
# The algorithm moves the right pointer to the right until it reaches the end of the string or encounters a repeating character.
# If the character at the right pointer is not in the set, the algorithm adds the character to the set and updates the maximum length of the substring if necessary.
# If the character at the right pointer is already in the set, the algorithm removes the character at the left pointer from the set and moves the left pointer to the right.
# The algorithm repeats this process until the right pointer reaches the end of the string.
# Finally, the algorithm returns the maximum length of the substring.
# This algorithm has a time complexity of O(n) and a space complexity of O(min(n, m)), where n is the length of the input string and m is the size of the character set.


def main(s):
    # Create an empty set to store unique characters
    char_set = set()
    # Initialize the maximum length to 0
    max_length = 0
    # Initialize the left and right pointers to 0
    left, right = 0, 0

    # Iterate over the string until the right pointer reaches the end
    while right < len(s):
        # If the character at the right pointer is not in the set
        if s[right] not in char_set:
            # Add the character to the set
            char_set.add(s[right])
            # Update the maximum length if necessary
            max_length = max(max_length, right - left + 1)
            # Move the right pointer to the right
            right += 1
        else:  # If the character at the right pointer is already in the set
            # Remove the character at the left pointer from the set
            char_set.remove(s[left])
            # Move the left pointer to the right
            left += 1

    # Return the maximum length of the substring
    return max_length
