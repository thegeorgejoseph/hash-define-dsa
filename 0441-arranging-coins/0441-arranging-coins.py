class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            k = left + ((right-left)//2)
            total = (k * (k + 1)) // 2
            if total == n:
                return k
            if total > n:
                right = k - 1
            else:
                left = k + 1
        return right