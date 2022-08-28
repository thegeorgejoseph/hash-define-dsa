class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counter = {}
        res = []
        for n in nums:
            Counter[n] = 1 + Counter.get(n, 0)
        freqs = [[] for i in range(len(nums) +1)]
        for n, count in Counter.items():
            freqs[count].append(n)
        for i in range(len(freqs)-1,-1,-1):
            for n in freqs[i]:
                if not freqs[i]: continue
                res.append(n)
                if len(res) == k:
                    return res
