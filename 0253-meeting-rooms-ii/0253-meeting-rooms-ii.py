class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        res, rooms = 0, 0
        left, right = 0, 0
        while left < len(intervals) and right < len(intervals):
            if starts[left] < ends[right]:
                rooms += 1
                left += 1
            else:
                rooms -= 1
                right += 1
            res = max(res, rooms)
        return res