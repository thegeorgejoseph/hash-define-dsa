class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        previousInterval = intervals[0]
        
        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] >= previousInterval[1]:
                previousInterval[1] = newInterval[1]
            else:
                res += 1
                previousInterval[1] = min(previousInterval[1], newInterval[1])
        
        return res