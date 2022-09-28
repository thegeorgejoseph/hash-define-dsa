class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        postfix_sum = []
        postfix  = 0
        for i in range(len(shifts)-1,-1,-1):
            postfix += shifts[i]
            postfix_sum.append(postfix)
        postfix_sum = postfix_sum[::-1]
        res = []
        for i, char in enumerate(s):
            new_char = chr(((ord(char)-ord('a') + postfix_sum[i]) % 26) + ord('a'))
            res.append(new_char)
        return "".join(res)