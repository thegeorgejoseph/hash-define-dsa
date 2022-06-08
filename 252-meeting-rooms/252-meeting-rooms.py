class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
#         Python you can sort a mutable object like list using .sort(key = lambda x: x[0])
        if not intervals:
            return True
        intervals.sort(key = lambda x: x[0])
        previousInterval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < previousInterval[1]:
                return False
            previousInterval = interval
        return True