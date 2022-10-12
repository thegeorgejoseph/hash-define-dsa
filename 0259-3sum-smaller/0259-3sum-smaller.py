class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        nums.sort()
        for i, num in enumerate(nums):
            # if i > 0 and num == nums[i-1]:
            #     continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total >= target:
                    # we need to find something smaller so move right - 1
                    right -= 1
                else:
                    # the array is sorted and if nums[i] + nums[left] + nums[right] < target then everything between left and right is less than target we can move the left pointer to find another triplet
                    res += right - left
                    left += 1
        return res
                    