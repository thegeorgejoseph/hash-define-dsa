class Solution:
    def sumOfDigits(self, n):
        _sum = 0
        while n > 0:
            _sum += pow(n % 10, 2)
            n = n // 10
        return _sum
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow, fast = self.sumOfDigits(slow), self.sumOfDigits(self.sumOfDigits(fast))
            if fast == 1:
                break
            if slow == fast:
                return False
        return fast == 1
        
            
#     def isHappy(self, n: int) -> bool:
#         visit = set()
#         while n != 1:
#             if n in visit:
#                 return False
#             visit.add(n)
#             n = self.sumOfDigits(n)
            
#         return True