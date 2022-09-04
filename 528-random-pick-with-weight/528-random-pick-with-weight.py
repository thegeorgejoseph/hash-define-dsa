class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix = 0
        for num in w:
            prefix += num
            self.prefix_sum.append(prefix)
        self.total = prefix

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        left, right = 0, len(self.prefix_sum) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()