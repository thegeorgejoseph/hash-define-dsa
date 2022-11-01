'''
[1,3,5,2,4]
[6,5,4,3,2,1,7]


'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        cache = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1][1] < num:
                prevIdx, prev = stack.pop()
                cache[prev]  = num
            stack.append((i, num))
        while stack:
            idx, node = stack.pop()
            cache[node] = -1
        res = []
        for num in nums1:
            if num not in cache:
                res.append(-1)
            else:
                res.append(cache[num])
        return res