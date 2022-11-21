class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i, newInterval in enumerate(intervals[1:]):
            curInterval = res[-1]
            if newInterval[0] > curInterval[1]:
                res.append(newInterval)
            else:
                curInterval = res.pop()
                curInterval = [min(curInterval[0], newInterval[0]), max(curInterval[1], newInterval[1])]
                res.append(curInterval)
        
        return res
        