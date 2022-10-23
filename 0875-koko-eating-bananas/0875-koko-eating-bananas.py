class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right + 1
        while left <= right:
            hours = 0
            k = left + ((right-left)//2)
            for n in piles:
                hours += math.ceil(n / k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res