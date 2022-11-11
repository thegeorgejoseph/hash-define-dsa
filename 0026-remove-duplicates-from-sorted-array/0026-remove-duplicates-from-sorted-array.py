class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIdx = 0
        for i in range(len(nums)):
            num = nums[i]
            if insertIdx == 0 or num != nums[insertIdx-1]:
                nums[insertIdx] = num
                insertIdx += 1
        return insertIdx