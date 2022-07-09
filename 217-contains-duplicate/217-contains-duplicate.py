class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
        # O(n) T O(n) S algorithm 
        # visited = {}
        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited[num] = True
        # return False
        # O(n**2) ST algorithm
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False 