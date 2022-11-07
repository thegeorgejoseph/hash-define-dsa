'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
res = [[1,3]]
curInterval = res[-1]
newInterval = [2,6]
pop, Merge, append
Intervals.sort()


'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i, newInterval in enumerate(intervals[1:]):
            curInterval = res[-1]
            if newInterval[0] > curInterval[1]:
                res.append(newInterval)
            else:
                prev = res.pop()
                curInterval = [min(prev[0], newInterval[0]), max(prev[1], newInterval[1])]
                res.append(curInterval)
        return res