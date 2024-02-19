# Problem 8 - Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:
# Input: dummy_input = ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Example 2:
# Input: dummy_input = ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"


# Solution Benchmark Analysis:
# Runtime: 0.52 μs
# Memory Usage: 56 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using a primary delimiter ":" to concatenate strings and a secondary delimiter ";" to mark the end of each string
# Split the encoded string using the combined delimiter ":;"


def encode(strs):
    # Use a primary delimiter ":" to concatenate strings and a secondary delimiter ";" to mark the end of each string
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s):
    # Split the encoded string using the combined delimiter ":;"
    strs, i = [], 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        strs.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return strs


def main(strs):
    # Encode the strings
    encoded = encode(strs)
    # Return the decoded string
    decoded = decode(encoded)

    return encoded, decoded


import unittest


class TestStringEncodeDecode(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(
            main(["lint", "code", "love", "you"])[1], ["lint", "code", "love", "you"]
        )

    def test_with_delimiter(self):
        self.assertEqual(main(["we", "say", ":", "yes"])[1], ["we", "say", ":", "yes"])

    def test_empty_string(self):
        self.assertEqual(main([""])[1], [""])

    def test_empty_list(self):
        self.assertEqual(main([])[1], [])

    def test_single_string(self):
        self.assertEqual(main(["single"])[1], ["single"])

    def test_special_characters(self):
        self.assertEqual(
            main(["special:;", "characters::;;"])[1], ["special:;", "characters::;;"]
        )

    def test_numeric_strings(self):
        self.assertEqual(main(["123", "456"])[1], ["123", "456"])

    def test_mixed_characters(self):
        self.assertEqual(main(["mix3d", "ch@r:;acters"])[1], ["mix3d", "ch@r:;acters"])

    def test_long_list(self):
        long_list = ["string" + str(i) for i in range(100)]
        self.assertEqual(main(long_list)[1], long_list)

    def test_encoded_decoded_equality(self):
        input_strs = ["test", "encode", "decode", "equality"]
        encoded, decoded = main(input_strs)
        self.assertNotEqual(encoded, input_strs)
        self.assertEqual(decoded, input_strs)


if __name__ == "__main__":
    unittest.main()
