class Solution:
    def isHappy(self, n: int) -> bool:
#         variation of Floyd Warshall's Algorithm to find cycles

        def get_next(n):
            result = 0
            while n :
                n, remainder = divmod(n, 10)
                result += remainder ** 2
            return result
        
        slow = n
        fast = get_next(n) #start the fast pointer from the next one
        while fast != 1 and fast != slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1