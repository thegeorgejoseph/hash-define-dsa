class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            currentInterval = res[-1]
            newInterval = intervals[i]
            if newInterval[0] > currentInterval[1]:
                res.append(newInterval)
            else:
                res.pop()
                newInterval = [min(currentInterval[0], newInterval[0]), max(currentInterval[1], newInterval[1])]
                res.append(newInterval)
        return res