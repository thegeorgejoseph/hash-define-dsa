class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we need to sort by the start times
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            elif start > lastEnd:
                res.append([start,end])
        return res