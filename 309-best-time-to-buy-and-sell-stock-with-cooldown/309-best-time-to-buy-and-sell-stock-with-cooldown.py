class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in cache:
                return cache[(i,canBuy)]
            
            if canBuy:
                buy = dfs(i + 1, not canBuy) - prices[i]
                cooldown = dfs(i + 1, canBuy)
                res = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not canBuy) + prices[i]
                cooldown = dfs(i + 1, canBuy)
                res = max(sell, cooldown)
            
            cache[(i, canBuy)] = res
            return res
        
        
        return dfs(0, True)