class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        suffix_sum = []
        greatestSoFar = 0
        for num in nums[::-1]:
            suffix_sum.append(greatestSoFar) if greatestSoFar > num else suffix_sum.append(0)
            greatestSoFar = max(greatestSoFar, num)
        suffix_sum = suffix_sum[::-1]
        res = -1
        for i in range(len(suffix_sum)):
            if suffix_sum[i] != 0:
                res = max(res, abs(suffix_sum[i]-nums[i]))
        return res