'''
Input: coins = [1,2,5] -> coin, amount = 11
[0,1,2,3,4,5,6,7,8,9,10,11] -> amt
[0,1,1,2,2,1,2,2,3,3,2,3]

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for amt in range(1, len(dp)):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1