class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                res += profit
            l += 1
            r += 1     
        return res
            