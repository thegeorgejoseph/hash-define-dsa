class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        currentInterval = intervals[0]
        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            # logic when they are not overlapping
            if newInterval[0] >= currentInterval[1]:
                currentInterval = newInterval[:]
            else:
                count += 1
                currentInterval = [min(currentInterval[0], newInterval[0]), min(currentInterval[1], newInterval[1])]
            
        return count
