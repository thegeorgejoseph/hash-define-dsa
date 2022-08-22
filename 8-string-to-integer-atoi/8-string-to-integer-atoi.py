class Solution:
    def myAtoi(self, s: str) -> int:
        # how to find convert a string number to integer? -> use ord('char') - ord('a') to get actual integer number
        # how to create a number from left to right? -> use char * 10 + new char to get the number, try with 789 example. -> This handles leading 0s case automatically.
        # how to strip leading and trailing spaces? -> use Python.strip()
        s = s.strip()
        negative = False
        INT_MIN, INT_MAX = -pow(2,31), pow(2,31) - 1
        res = 0
        if not s:
            return 0
        if s[0] == "-":
            negative = True
        elif s[0] == "+":
            negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            res = ord(s[0]) - ord("0")
        
        for i in range(1, len(s)):
            if s[i].isnumeric():
                res = res*10 + (ord(s[i]) - ord("0"))
                if res > INT_MAX and negative:
                    return INT_MIN
                elif res > INT_MAX and not negative:
                    return INT_MAX
                
            else:
                break
        
        if not negative:
            return res
        else:
            return -res
        