'''
[1,2,3,1,0,0]
[4 ,3,3,1]

[2,7,9,3,1,0,0]
[12,10,10,3,1]
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums[::-1]:
            temp = rob2
            rob2 = max(num + rob1, rob2)
            rob1 = temp
        return rob2