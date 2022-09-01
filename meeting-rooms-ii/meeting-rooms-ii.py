class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([j[1] for j in intervals])
        i,j,count,res = 0,0,0,0
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res