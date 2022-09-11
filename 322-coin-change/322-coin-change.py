class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0     
        for amt in range(1, len(dp)):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1