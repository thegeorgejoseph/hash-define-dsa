class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # three conditions 
        # condition to place the new interval before the rest of the array
        # condition to place the new interval after the rest of the array
        # condition to place the new interval as a merged array
        res = []
        for i in range(len(intervals)):
            currentInterval = intervals[i]
            if newInterval[0] < currentInterval[0] and newInterval[1] < currentInterval[0]:
                res.append(newInterval)
                return res + intervals[i : ]
            elif newInterval[0] > currentInterval[1]:
                res.append(currentInterval)
            else:
                newInterval = [min(newInterval[0], currentInterval[0]),max(newInterval[1], currentInterval[1])]
        res.append(newInterval)
        return res
    
    