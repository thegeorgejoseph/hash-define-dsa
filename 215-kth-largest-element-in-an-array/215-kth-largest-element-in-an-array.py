class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            if l == r:
                return nums[l]
            
            p = l
            pivot = nums[r]
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
            
        return quickSelect(0, len(nums) - 1)

        # nums = [-1 * n for n in nums]
        # heapq.heapify(nums)
        # while k > 1:
        #     heapq.heappop(nums)
        #     k -= 1
        # print(nums)
        # return nums[0] * -1
        # return sorted(nums)[len(nums) - k]