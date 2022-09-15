class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        prefix = 0
        self.prefix_sum = []
        for n in w:
            prefix += n
            self.prefix_sum.append(prefix)

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        left, right = 0, len(self.prefix_sum)-1
        while left <= right:
            mid = left + ((right-left)//2)
            pivot = self.prefix_sum[mid]
            if target > pivot:
                left = mid + 1
            else:
                right = mid - 1
        return left

