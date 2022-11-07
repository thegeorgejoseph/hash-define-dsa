'''
Input: intervals = [[1,4],[3,6],[2,8]]
[[1,4],[2,8],[3,6]]
[[1,8]]
output = 2
Input: intervals = [[1,4],[2,3]]
[[1,4]]
1

c---- a ---- b ---- d
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        curInterval = intervals[0]
        remove = 0
        for i in range(1,len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] > curInterval[1]:
                curInterval = newInterval[:]
            elif newInterval[0] <= curInterval[1] and newInterval[1] <= curInterval[1]:
                remove += 1
            else:
                curInterval = [min(curInterval[0], newInterval[0]), max(curInterval[1], newInterval[1])]
        return len(intervals)-remove