class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            idx = abs(nums[i])
            if 1 <= idx <= len(nums):
                if nums[idx-1] > 0:
                    nums[idx-1] *= -1
                elif nums[idx-1] == 0:
                    nums[idx-1] = float('-inf')
            
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0: return i
        return len(nums) + 1
        
        
        
            
        