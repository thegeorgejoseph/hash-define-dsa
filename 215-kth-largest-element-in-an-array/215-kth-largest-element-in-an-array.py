class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        print(nums)
        return nums[0] * -1
        # return sorted(nums)[len(nums) - k]