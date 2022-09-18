class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        res = []
        intervals.sort(key = lambda x: x[0])
        currentInterval = intervals[0]
        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] > currentInterval[1]:
                res.append(currentInterval)
                currentInterval = newInterval
            else:
                currentInterval = [min(currentInterval[0], newInterval[0]), max(currentInterval[1], newInterval[1])]
        res.append(currentInterval)
        return res