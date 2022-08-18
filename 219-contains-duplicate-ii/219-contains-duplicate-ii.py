class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = set()
        for i, num in enumerate(nums):
            if num in cache:
                return True
            cache.add(num)
            if len(cache) > k:
                cache.remove(nums[i - k])
        return False