class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-1 * n for n in nums]
        heapq.heapify(maxHeap)
        count = 0
        while maxHeap:
            largest = heapq.heappop(maxHeap)
            count += 1
            if count == k:
                return -largest
        