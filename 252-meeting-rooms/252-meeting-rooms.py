class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        currentInterval = intervals[0]
        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] < currentInterval[1]:
                return False
            currentInterval = [min(currentInterval[0], newInterval[0]), max(currentInterval[1], newInterval[1])]
        return True