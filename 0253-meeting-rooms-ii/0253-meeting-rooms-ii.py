class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        starts = sorted([n[0] for n in intervals])
        ends = sorted([n[1] for n in intervals])
        i, j, count = 0, 0, 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
            
        return res