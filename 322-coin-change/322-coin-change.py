class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #the default value does not have to be infinity
        dp[0] = 0 # base case
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt-coin])
        return dp[amount] if dp[amount] != amount + 1 else -1