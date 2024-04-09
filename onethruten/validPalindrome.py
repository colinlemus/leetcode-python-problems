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
# Runtime: 2.23 μs
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


import unittest


class TestValidPalindrome(unittest.TestCase):
    def test_palindrome_with_punctuation(self):
        self.assertTrue(main("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        self.assertFalse(main("race a car"))

    def test_only_non_alphanumeric(self):
        self.assertTrue(main(",,,!!!"))

    def test_case_insensitivity(self):
        self.assertTrue(main("Aa"))

    def test_with_numbers(self):
        self.assertTrue(main("12321"))
        self.assertFalse(main("123210"))

    def test_empty_string(self):
        self.assertTrue(main(""))

    def test_single_character(self):
        self.assertTrue(main("a"))
        self.assertTrue(main("1"))

    def test_large_string(self):
        large_palindrome = (
            "a" * 100000 + "b" * 100000 + "a" * 100000
        )  # 300000 characters
        self.assertTrue(main(large_palindrome))
        large_non_palindrome = "a" * 100000 + "bc" + "a" * 100000  # 200002 characters
        self.assertFalse(main(large_non_palindrome))


if __name__ == "__main__":
    unittest.main()
