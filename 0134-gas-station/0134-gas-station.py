class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        i = 0
        tank = 0
        res = 0
        while i < len(gas):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                res = i + 1
            i += 1
        return res