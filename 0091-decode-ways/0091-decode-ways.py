'''
s = 12
you can take just one character irrespective of what it is 
except 0 if 0 return 0
if you want to take the second character as well then we should 
consider if first character 1 then any if 2 then between 1-6.
recursive dfs
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}
        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if i + 1< len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            cache[i] = res
            return res
        return dfs(0)