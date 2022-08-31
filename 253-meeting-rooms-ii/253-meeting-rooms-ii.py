class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([j[1] for j in intervals])
        i, j = 0, 0
        count = 0
        res = 0
        
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        
        return res