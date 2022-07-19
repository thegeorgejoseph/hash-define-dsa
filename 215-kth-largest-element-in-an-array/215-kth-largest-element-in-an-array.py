class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l,r):
            if l == r:
                return nums[l]
            p, pivot = l, nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickSelect(l, p- 1)
            if p < k:
                return quickSelect(p+ 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums)-1)
        # return sorted(nums)[len(nums)-k]
        # k = len(nums) - k
        # heapq.heapify(nums)
        # top = None
        # while k > 0:
        #     heapq.heappop(nums)
        #     k -= 1
        # return nums[0]