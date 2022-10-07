class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        res = [[] for _ in range(len(nums)  + 1)]
        for el, i in freqs.items():
            res[i].append(el)
        result = []
        for i in range(len(res)-1, -1, -1):
            for el in res[i]:
                result.append(el)
            if len(result) == k:
                return result
        return result
        
        
        
        
        # freqs = {}
        # for num in nums:
        #     freqs[num] = 1 + freqs.get(num, 0)
        # maxHeap = []
        # for item, freq in freqs.items():
        #     heapq.heappush(maxHeap, (-freq, item))
        # res = []
        # while maxHeap:
        #     _, el = heapq.heappop(maxHeap)
        #     res.append(el)
        #     if len(res) == k:
        #         return res
        # return res