class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if num in visited:
                return True
            visited[num] = True
        return False
        # O(n**2) algorithm
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False 