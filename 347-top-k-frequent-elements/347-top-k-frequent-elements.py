class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         Bucket sort technique
# Make a hash-map that stores all the counts
# then create another list if you want that stores the indices as the count and the values as lists with the numbers that are of that particular count.
        cache = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            cache[n] = cache.get(n,0) + 1
        for n, c in cache.items():
            freq[c].append(n)
        
        res = []
        
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res