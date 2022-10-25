'''
[10,15,20,0]
min(15 + 0, 15 + 20 ) = 15
min(10 + 15[cost computed], 10 + 20[computed cost])
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:]
        dp.append(0)
        for i in range(len(dp)-3,-1,-1):
            dp[i] = min(dp[i] + dp[i + 1], dp[i] + dp[i + 2])
        return min(dp[0], dp[1])