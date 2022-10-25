'''
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        res = 0
        while left < len(prices) and right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right = right
            else:
                res += profit
                left = right
                right = right
            right += 1
        return res