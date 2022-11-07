
'''
Input: intervals = [[0,30],[5,10],[15,20]]
starts = [0,5,15]
ends = [10,20,30]
whenever a meeting starts before a meeting ends rooms += 1
whenever a meeting ends, rooms -= 1
update global res
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res, i, j, rooms = 0, 0, 0, 0
        starts = sorted([vals[0] for vals in intervals])
        ends = sorted([vals[1] for vals in intervals])
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            res = max(res, rooms)
        return res