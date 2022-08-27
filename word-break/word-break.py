class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(dp) -2, -1, -1):
            for word in wordDict:
                j = len(word)
                if i + j <= len(s) and s[i:i+j] == word:
                    dp[i] = dp[i+j]
                if dp[i]:
                    break
        return dp[0]