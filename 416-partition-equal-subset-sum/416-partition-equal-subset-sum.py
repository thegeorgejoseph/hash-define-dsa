class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        total = total // 2
        
        dp = set([0])
        
        for num in nums:
            for val in dp.copy():
                if num + val == total:
                    return True
                dp.add(num + val)
        return False
        
        
        
        # if sum(nums) % 2 == 1:
        #     return False
        # target = sum(nums) // 2
        # dp = set()
        # dp.add(0)
        # for i in range(len(nums)-1,-1,-1):
        #     for curTarg in dp.copy():
        #         if nums[i] + curTarg == target:
        #             return True
        #         dp.add(nums[i]+curTarg)
        # return False
            