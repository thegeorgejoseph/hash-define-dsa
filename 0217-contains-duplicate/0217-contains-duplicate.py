class Solution:
    def __init__(self):
        self.cache = set()
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            if n in self.cache:
                return True
            self.cache.add(n)
        return False