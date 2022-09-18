class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counter = {}
        for num in nums:
            Counter[num] = 1 + Counter.get(num,0)
        
        maxHeap = []
        for num, count in Counter.items():
            heapq.heappush(maxHeap, (-count, num))
        res = []
        while maxHeap:
            cnt, num = heapq.heappop(maxHeap)
            res.append(num)
            if len(res) == k:
                return res
        return res
#         Counter = {}
#         for num in nums:
#             Counter[num] = 1 + Counter.get(num, 0)
        
#         temp = [[] for i in range(len(nums)+1)]
#         for key, value in Counter.items():
#             temp[value].append(key)
#         res = []
#         for i in range(len(temp)-1,-1,-1):
#             if not temp[i]:
#                 continue
#             for n in temp[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
        
#         Counter = {}
#         for num in nums:
#             Counter[num] = 1 + Counter.get(num, 0)
        
#         maxHeap = [(-value, key) for key, value in Counter.items()]
#         heapq.heapify(maxHeap)
#         res = []
#         while maxHeap:
#             value, ele = heapq.heappop(maxHeap)
#             res.append(ele)
#             if len(res) == k:
#                 break
#         return res