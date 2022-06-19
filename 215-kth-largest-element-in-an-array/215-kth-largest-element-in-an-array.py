class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        heapq.heapify(nums)
        top = None
        while k > 0:
            heapq.heappop(nums)
            k -= 1
        return nums[0]