class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums)-k]
        # k = len(nums) - k
        # heapq.heapify(nums)
        # top = None
        # while k > 0:
        #     heapq.heappop(nums)
        #     k -= 1
        # return nums[0]