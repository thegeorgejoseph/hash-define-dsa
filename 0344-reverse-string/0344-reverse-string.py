class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)
        for i in range(len(s)):
            s[i] = stack.pop()
        return s
#         l, r = 0, len(s)-1
#         def reverse(l,r):
#             if l >= r:
#                 return 
            
#             s[l], s[r] = s[r], s[l]
#             reverse(l + 1, r - 1)
        
#         reverse(l, r)
#         return s
        # l, r = 0, len(s) - 1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l, r = l + 1, r - 1
        # return s
        