class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda x: x[0])
        curInterval = intervals[0]
        for i, newInterval in enumerate(intervals[1:]):
            if newInterval[0] < curInterval[1]:
                return False
            curInterval = newInterval[:]
        return True