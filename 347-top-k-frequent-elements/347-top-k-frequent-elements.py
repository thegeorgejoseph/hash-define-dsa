class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counter = {}
        res = []
        for n in nums:
            Counter[n] = 1 + Counter.get(n, 0)
        
        freqs = [[] for _ in range(len(nums) +1)]
        for num, count in Counter.items():
            freqs[count].append(num)
        for i in range(len(freqs) - 1, -1, -1):
            if not freqs[i]:
                continue
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res
        