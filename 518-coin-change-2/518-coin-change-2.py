class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, total):
            if i == len(coins):
                return 0
            if (i, total) in cache:
                return cache[(i,total)]
            if total == amount:
                return 1
            if total > amount:
                return 0 
            
            cache[(i,total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return cache[(i,total)]
        
        return dfs(0,0)