class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counter = {}
        res = []
        for num in nums:
            Counter[num] = Counter.get(num, 0) + 1
        
        maxHeap = []
        for key, value in Counter.items():
            heapq.heappush(maxHeap, (-value, key))
        
        while maxHeap:
            value, key = heapq.heappop(maxHeap)
            res.append(key)
            if len(res) == k:
                return res
        return res
        
        # Counter = {}
        # res = []
        # for n in nums:
        #     Counter[n] = 1 + Counter.get(n, 0)
        # freqs = [[] for i in range(len(nums) +1)]
        # for n, count in Counter.items():
        #     freqs[count].append(n)
        # for i in range(len(freqs)-1,-1,-1):
        #     for n in freqs[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
