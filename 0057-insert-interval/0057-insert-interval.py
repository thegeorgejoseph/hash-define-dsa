class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, curInterval in enumerate(intervals):
            if newInterval[1] < curInterval[0]:
                res.append(newInterval)
                return res + intervals[i :]
            elif newInterval[0] > curInterval[1]:
                res.append(curInterval)
            else:
                newInterval = [min(curInterval[0], newInterval[0]), max(curInterval[1], newInterval[1])]
        res.append(newInterval)
        return res