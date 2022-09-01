class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSumLeft, prefixSumRight = [], []
        prefixL = 0
        for n in nums:
            prefixL = n + prefixL
            prefixSumLeft.append(prefixL)
        prefixR = 0
        for n in nums[::-1]:
            prefixR = n + prefixR
            prefixSumRight.append(prefixR)
        
        prefixSumRight = prefixSumRight[::-1]
        for i in range(len(nums)):
            if prefixSumLeft[i] == prefixSumRight[i]:
                return i
        return -1