'''
Straight Forward solution - hashmap O(N)ST
Boyer Moore's Voting Algorithm - O(N)T O(1) space
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0 and num != res:
                res = num
                count = 1
                continue
            if num == res:
                count += 1
            else:
                count -= 1
        return res