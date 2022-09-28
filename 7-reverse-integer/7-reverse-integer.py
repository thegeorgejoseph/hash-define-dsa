class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            
            if (res > INT_MAX // 10 or (res == INT_MAX // 10 and digit >= INT_MAX % 10)):
                return 0
            if (res < INT_MIN // 10 or (res == INT_MIN // 10 and digit <= INT_MIN % 10)):
                return 0
            res = res*10 + digit
        return res