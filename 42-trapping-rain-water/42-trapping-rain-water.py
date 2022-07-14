class Solution:
    def trap(self, height: List[int]) -> int:
        nums= height
        prefix = [i for i in height]
        
        for i in range(1,len(height)):
            prefix[i] = max(prefix[i-1], nums[i-1])
        
        suffix = [i for i in height]
        
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i+1], nums[i+1])
        
        res = [0] * (len(height) )
        
        for i in range(len(height)):
            temp = min(prefix[i], suffix[i]) - nums[i]
            res[i] = temp if temp >= 0 else 0
        
        return sum(res)