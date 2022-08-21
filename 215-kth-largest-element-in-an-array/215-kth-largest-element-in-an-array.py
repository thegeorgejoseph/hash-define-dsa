class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            if l == r:
                return nums[l]
            
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if k > p:
                return quickSelect(p + 1, r)
            elif k < p:
                return quickSelect(l, p - 1)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) -1)