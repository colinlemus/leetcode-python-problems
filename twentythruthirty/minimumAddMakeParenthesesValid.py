# Problem 21 - Minimum Add to Make Parentheses Valid

# A parentheses string is valid if and only if:
#     It is the empty string,
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.

# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1

# Example 2:
# Input: s = "((("
# Output: 3

# Constraints:
#     1 <= s.length <= 1000
#     s[i] is either '(' or ')'.

# Solution Benchmark Analysis:
# Runtime: 0.3858 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:


def main(s):
    # Create an empty stack to store opening parentheses
    stack = []

    # Create a counter to keep track of the number of unmatched opening parentheses
    count = 0

    for char in s:
        # If the current character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the current character is a closing parenthesis, pop the top element from the stack
        elif char == ")":
            if stack:
                stack.pop()
            # If the stack is empty, the current closing parenthesis is unmatched, so we increment the counter
            else:
                count += 1

    # The number of unmatched opening parentheses is equal to the number of elements in the stack
    count += len(stack)

    return count
