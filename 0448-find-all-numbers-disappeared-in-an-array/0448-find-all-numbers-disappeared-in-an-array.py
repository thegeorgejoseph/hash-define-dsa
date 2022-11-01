class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        print(nums)
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                res.append(i)
        return res