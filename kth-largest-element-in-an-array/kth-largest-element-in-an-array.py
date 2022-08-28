class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        
        def quickSelect(l,r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            if k < p:
                return quickSelect(l, p - 1)
            elif k > p:
                return quickSelect(p + 1,r)
        
        return quickSelect(0, len(nums) -1)
            
        