class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        else:
            total = total // 2
        
        dp = set([0])
        
        for num in nums:
            for val in dp.copy():
                if num + val == total:
                    return True
                dp.add(num + val)
        
        return False