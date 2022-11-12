class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        res = 0
        while left <= right:
            mid = left + ((right-left)//2)
            total = mid * (mid + 1) // 2
            if total > n:
                right = mid - 1
            else:
                left = mid + 1
                res = max(res, mid)
        return res