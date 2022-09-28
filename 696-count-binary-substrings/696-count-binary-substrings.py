# '''
# 00110011
# -> 2, 2, 2, 2
# -> 2 + 2 + 2 = 6
# 10101
# -> 1, 1, 1, 1, 1
# ->4 
# 00110
# -> 2,2,1
# Find all the consecutive group lengths
# and find the min(every pair) and sum them
# '''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        temp = 0
        i = 0
        res = 0
        while i < len(s):
            if i > 0 and s[i] != s[i-1]:
                groups.append(temp)
                temp = 0
            temp += 1
            i += 1
        groups.append(temp)
        for i in range(0, len(groups)-1):
            a = groups[i]
            b = groups[i + 1] 
            res += min(a,b)
        return res