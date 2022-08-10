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
             
        
#         variation of Floyd Warshall's Algorithm to find cycles

#         def get_next(n):
#             result = 0
#             while n :
#                 n, remainder = divmod(n, 10)
#                 result += remainder ** 2
#             return result
        
#         slow = n
#         fast = get_next(n) #start the fast pointer from the next one
#         while fast != 1 and fast != slow:
#             slow = get_next(slow)
#             fast = get_next(get_next(fast))
            
#         return fast == 1