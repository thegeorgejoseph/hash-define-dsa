class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        left, right = 1, num // 2
        while left <= right:
            candidate = left + ((right-left)>>1)
            _square = candidate**2
            if _square == num:
                return True
            if _square < num:
                left = candidate + 1
            else:
                right = candidate - 1
        return False