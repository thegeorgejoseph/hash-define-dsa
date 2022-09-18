class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        res, rooms = 0, 0
        i, j = 0, 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            res = max(res, rooms)
            
        return res
                