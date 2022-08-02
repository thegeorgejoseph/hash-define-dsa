class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x[0])
        previousInterval = intervals[0]
        
        for i in range(1,len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] < previousInterval[1]:
                return False
            previousInterval = [min(previousInterval[0], newInterval[0]),max(previousInterval[1], newInterval[1])]
        
        return True