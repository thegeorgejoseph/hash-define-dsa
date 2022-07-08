class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if you choose the largest number then no. of hours needed = len(piles)
        # if you choose the smallest number then add up each math.ceil(p / k)
        # run Binary search between 1 and largest number and find the smallest value of k
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            k = left + ((right - left) // 2)
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res