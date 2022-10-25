'''
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


**may be reused multiple times
[l,e,e,t,c,o,d,e,""]
[T,F,F,F,T,F,F,F,T] -> when you find a word in wordDict that gives True, break
-> if dp[0] == True, ret True


'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[-1] = True
        for i in range(len(dp)-2, -1, -1):
            for word in wordDict:
                j = len(word)
                if i + j < len(dp) and s[i: i + j] == word:
                    dp[i] = dp[i + j]
                    if dp[i]: break
        return dp[0]