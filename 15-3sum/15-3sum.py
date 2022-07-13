class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort() 
        #why do you keep forgetting to sort it?
        for index, num in enumerate(nums):
            # we need to ensure that we are not starting from the same number again too!
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left, right = index + 1, n - 1
            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res