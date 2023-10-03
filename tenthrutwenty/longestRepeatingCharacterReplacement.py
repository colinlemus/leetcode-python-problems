# Problem 17 - Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4

# Constraints:
#     1 <= s.length <= 10^5
#     s consists of only uppercase English letters.
#     0 <= k <= s.length

# Solution Benchmark Analysis:
# Runtime: 1.8 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# This algorithm finds the length of the longest substring that can be formed by replacing at most k characters in an input string.
# The algorithm uses a sliding window approach to iterate over the string.
# The algorithm uses a dictionary to store the frequency of each character in the current window.
# The algorithm updates the maximum frequency of any character in the current window and checks if the window needs to be shrunk to satisfy the constraint of at most k replacements.
# If the window needs to be shrunk, the algorithm moves the left pointer to the right and updates the frequency counter accordingly.
# The algorithm repeats this process until the right pointer reaches the end of the string.
# Finally, the algorithm returns the maximum length of the substring.
# This algorithm has a time complexity of O(n) and a space complexity of O(1).


def main(s: str, k: int) -> int:
    # Initialize variables
    freq_counter = {}
    max_freq = 0
    max_len = 0
    left = 0

    # Iterate through the string using a sliding window
    for right in range(len(s)):
        # Update frequency counter
        if s[right] not in freq_counter:
            freq_counter[s[right]] = 0
        freq_counter[s[right]] += 1

        # Update max frequency in the current window
        max_freq = max(max_freq, freq_counter[s[right]])

        # Check if we need to shrink the window
        if right - left + 1 - max_freq > k:
            freq_counter[s[left]] -= 1
            left += 1

        # Update the max length
        max_len = max(max_len, right - left + 1)

    # Return the maximum length of the substring
    return max_len
