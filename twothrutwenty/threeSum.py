# Problem 12 - 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = [0,1,1]
# Output: []

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]

# Constraints:
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

# Solution Benchmark Analysis:
# Runtime: 2.7320 μs
# Memory Usage: 88 bytes
# Time complexity: O(n^2)
# Space complexity: O(n)

# Explanation:
# The function uses a hash table to find all unique triplets in the nums list that add up to zero.
# The function first sorts the nums list in ascending order using the sort() method.
# The function then iterates over the nums list using a for loop. At each iteration, the function checks if the current element is a duplicate of the previous element. If it is, the function skips the current iteration using the continue statement.
# The function then creates an empty hash table called hash_table to store the values.
# The function then iterates over the nums list again using another for loop, starting from the current index i plus one. At each iteration, the function calculates the complement of the sum of the current element and the element at the current index i. The complement is the negative sum of the two elements.
# The function then checks if the complement is in the hash_table. If it is, the function appends a list containing the current element, the element at the current index i, and the complement to the output list. The function then skips all duplicates of the current element using a while loop.
# If the complement is not in the hash_table, the function adds the current element to the hash_table.
# Finally, the function returns the output list containing all unique triplets that add up to zero.
# Overall, this function is an efficient and optimal solution to the Three Sum problem, with a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the nums list.


def main(nums):
    # Sort the array
    nums.sort()
    output = []

    # Iterate over the array
    for i in range(len(nums)):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Create a hash table to store the values
        hash_table = {}

        # Iterate over the array again
        for j in range(i + 1, len(nums)):
            # Calculate the complement
            complement = -nums[i] - nums[j]

            # Check if the complement is in the hash table
            if complement in hash_table:
                # Append the triplet to the output
                output.append([nums[i], nums[j], complement])
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1

            # Add the value to the hash table
            hash_table[nums[j]] = j
    return output
