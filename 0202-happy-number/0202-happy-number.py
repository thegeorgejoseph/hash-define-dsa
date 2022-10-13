class Solution:
    def sumOfDigits(self, n):
        _sum = 0
        while n > 0:
            _sum += pow(n % 10, 2)
            n = n // 10
        return _sum
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1:
            if n in visit:
                return False
            visit.add(n)
            n = self.sumOfDigits(n)
            
        return True