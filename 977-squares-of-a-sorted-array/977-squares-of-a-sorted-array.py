class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums))
        left, right = 0, len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                temp = nums[right]
                right -= 1
            else:
                temp = nums[left]
                left += 1
            res[i] = pow(temp,2)
        return res