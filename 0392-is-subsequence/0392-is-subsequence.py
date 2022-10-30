'''

Two Pointers Solution


DP Levenshtein Distance Solution
    a  h  b  g  d  c  " "
a   T                  F
b         T        T   
c   5  4  3  2  1  0   1

Subsequence is like Levenshtein Distance with deletions, if number of deletions required is less than length of target

dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
        dp[-1][-1] = 0
        for i in range(len(s)):
            dp[i][len(t)] = len(s) - i
        for j in range(len(t)):
            dp[len(s)][j] = len(t) - j
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + 1
        
        return True if (len(t) - dp[0][0] >= len(s)) else False

'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False
        s_ptr, t_ptr = 0,0
        while t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                if s_ptr == len(s):
                    return True
            t_ptr += 1
        return False
                