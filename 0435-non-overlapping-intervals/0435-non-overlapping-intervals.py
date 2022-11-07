'''
Input: intervals = [[1,3], [1,2],[2,3],[3,4]]

intervals.sort()
1,2,3
1,2
remove the largest each time there is a merge conflict so that we minimise the future conflicts to be removed
curInterval = intervals[0]
newInterval = 

'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        curInterval = intervals[0]
        res = 0
        for i, newInterval in enumerate(intervals[1:]):
            if newInterval[0] >= curInterval[1]:
                curInterval = newInterval[:]
            else:
                res += 1
                curInterval = [min(curInterval[0], newInterval[0]), min(curInterval[1], newInterval[1])]
        return res
            
        