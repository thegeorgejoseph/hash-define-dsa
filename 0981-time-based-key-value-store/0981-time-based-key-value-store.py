class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.cache[key]
        if not values: return ""
        res = ""
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + ((right-left)//2)
            time, val = values[mid]
            if time == timestamp: return val
            if time < timestamp:
                res = val
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)