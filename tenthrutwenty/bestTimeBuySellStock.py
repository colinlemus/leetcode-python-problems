# Problem 15 - Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0

# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

# Solution Benchmark Analysis:
# Runtime: 1.38 μs
# Memory Usage: 28 bytes
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# This algorithm uses a greedy approach to find the maximum profit that can be obtained by buying and selling a stock.
# The idea is to keep track of the minimum price seen so far and the maximum profit that can be obtained by selling the stock at the current price.
# The algorithm updates the minimum price and maximum profit seen so far based on the current price, and returns the maximum profit seen so far.
# This algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.


def main(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
