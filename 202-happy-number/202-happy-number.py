class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSums(n):
            res = 0
            while n:
                res += (n % 10)**2
                n = n // 10
            return res
        slow, fast = n, squareSums(n)
        while fast != 1 and fast != slow:
            slow = squareSums(slow)
            fast = squareSums(squareSums(fast))
        
        return fast == 1
        
#         visit = set()
#         while n != 1:
#             if n in visit:
#                 return False
#             visit.add(n)
#             n = squareSums(n)
        
#         return True