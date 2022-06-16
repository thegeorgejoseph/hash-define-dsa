class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.store:
        #     self.store[key] = []
        #using defaultdict to make code smaller
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        nums = self.store.get(key, []) # best way to get from a dictionary 
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m][1] == timestamp:
                return nums[m][0]
            elif nums[m][1] < timestamp:
                res = nums[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)