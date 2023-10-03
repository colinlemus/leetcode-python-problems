# Problem 20 - Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
#     1 <= s.length <= 10^4
#     s consists of parentheses only '()[]{}'.

# Solution Benchmark Analysis:
# Runtime: 1.6368 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# This function checks if a string of parentheses is balanced, i.e., if each opening parenthesis has a corresponding closing parenthesis.
# The function uses a stack to keep track of opening parentheses.
# The function iterates over the string and pushes opening parentheses onto the stack.
# When a closing parenthesis is encountered, the function pops the top element from the stack and compares it to the corresponding opening parenthesis.
# If the opening parenthesis does not match the closing parenthesis, the function returns False.
# If the stack is empty at the end of the iteration, the function returns True (all parentheses are balanced), otherwise it returns False.
# This function has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.


def main(s):
    # Create an empty stack to store opening parentheses
    stack = []
    # Create a dictionary to map closing parentheses to opening parentheses
    mapping = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        if char in mapping.values():
            # If the character is an opening parenthesis, push it onto the stack
            stack.append(char)
        elif char in mapping.keys():
            # If the character is a closing parenthesis, pop the top element from the stack and compare it to the corresponding opening parenthesis
            top_element = stack.pop() if stack else "#"

            # If the opening parenthesis does not match the closing parenthesis, return False
            if mapping[char] != top_element:
                return False

    # If the stack is empty, return True (all parentheses are balanced), otherwise return False
    return not stack
