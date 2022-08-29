class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        nums = self.store[key]
        if not nums:
            return ""
        left, right = 0, len(nums) - 1
        res = ""
        while left <= right:
            mid = left + ((right - left) // 2)
            if timestamp == nums[mid][1]:
                return nums[mid][0]
            if timestamp < nums[mid][1]:
                right = mid - 1
            else:
                res = nums[mid][0]
                left = mid + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
