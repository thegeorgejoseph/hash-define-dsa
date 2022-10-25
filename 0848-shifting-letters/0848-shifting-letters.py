class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        postfix = 0
        postfix_sum = []
        for i in range(len(shifts)-1,-1,-1):
            postfix += shifts[i]
            postfix_sum.append(postfix)
        postfix_sum = postfix_sum[::-1]
        res = []
        for i, c in enumerate(s):
            digit = ord(c)-ord('a')
            res.append(chr(((digit + postfix_sum[i]) % 26) + ord('a')))
        return "".join(res)