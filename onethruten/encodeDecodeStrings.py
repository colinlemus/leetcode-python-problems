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
# Runtime: 0.5223 μs
# Memory Usage: 56 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# Using a primary delimiter ":" to concatenate strings and a secondary delimiter ";" to mark the end of each string
# Split the encoded string using the combined delimiter ":;"

def encode(strs):
    # Use a primary delimiter ":" to concatenate strings and a secondary delimiter ";" to mark the end of each string
    return ':;'.join(strs)

def decode(s):
    # Split the encoded string using the combined delimiter ":;"
    return s.split(':;')

def main(strs):
    # Encode the strings
    encoded = encode(strs)
    # Return the decoded string    
    decoded = decode(encoded)

    return encoded, decoded