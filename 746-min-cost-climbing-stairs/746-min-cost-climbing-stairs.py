class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        #base case 1 : to reach the goal from the goal it takes 0 cost
        #base case 2 : to reach the goal from the n - 1 it takes cost[n-1]
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
            
        return min(cost[0],cost[1])