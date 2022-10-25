'''
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


'''

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _min = min(nums)
        res = 0
        for n in nums:
            res += (n- _min)
        return res