class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                continue
            left, right = index + 1, n -1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0 :
                    right -= 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1 # why only left is updated? because the other two conditions handles the rest
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res