class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd Warshall's Tortoise and Hare Algorithm in Linked Lists using Arrays
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow