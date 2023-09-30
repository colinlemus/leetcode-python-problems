# Problem 18 - Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"

# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of English letters.

# Solution Benchmark Analysis:
# Runtime: 0.9973 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(m)

# Explanation:
# This algorithm finds the minimum window substring of s that contains all the characters in t.
# The algorithm uses a sliding window approach to iterate over the string.
# The algorithm uses a dictionary to store the frequency of each character in t and a defaultdict to store the frequency of each character in the current window.
# The algorithm expands the window to the right until it contains all the characters in t. The algorithm then shrinks the window from the left until it no longer contains all the characters in t.
# The algorithm repeats this process until the right pointer reaches the end of the string.
# Finally, the algorithm returns the minimum window substring if it exists, otherwise it returns an empty string.
# This algorithm has a time complexity of O(n) and a space complexity of O(m), where m is the size of the character set in t.

from collections import Counter, defaultdict


def main(s, t):
    # Create a dictionary to store the frequency of each character in t
    t_counter = Counter(t)
    # Create a defaultdict to store the frequency of each character in the current window
    s_counter = defaultdict(int)
    # Initialize the number of unique characters in t
    unique_chars = len(t_counter)
    # Initialize the left and right pointers to 0
    l, r = 0, 0
    # Initialize the minimum window size to infinity
    min_window = float("inf")
    # Initialize the minimum window string to an empty string
    min_window_str = ""

    # Iterate over the string using a sliding window
    while r < len(s):
        # Expand window to the right
        if s[r] in t_counter:
            s_counter[s[r]] += 1

            # Check if this character count matches that in t
            if s_counter[s[r]] == t_counter[s[r]]:
                unique_chars -= 1

        # Shrink window from the left
        while unique_chars == 0:
            if r - l < min_window:
                min_window = r - l
                min_window_str = s[l : r + 1]

            if s[l] in t_counter:
                s_counter[s[l]] -= 1
                if s_counter[s[l]] < t_counter[s[l]]:
                    unique_chars += 1

            l += 1

        # Move the right pointer
        r += 1

    # Return the minimum window string if it exists, otherwise return an empty string
    return min_window_str if min_window != float("inf") else ""
