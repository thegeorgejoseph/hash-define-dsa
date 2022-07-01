class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0: # required because -> s = ( * ) (
                leftMin = 0
        return leftMin == 0
#         Learn this stack solution too 
#         count = []
#         stack = []
# 		# we only add in (, and if we meet a ), we pop one (
# 		# if we meet a *, we add the index into count. We first assume all * is empty string.
#         for i, st in enumerate(s):
#             if st == "(":
#                 stack.append(i)
#             elif st == ")":
#                 if not stack and not count:
#                     return False
#                 elif not stack:
#                     count.pop()
#                 else:
#                     stack.pop()
#             else:
#                 count.append(i)
		
# 		# we finally ensure if stack has extra (, the * in count appear after (. 
#         while stack and count:
#             if stack.pop() > count.pop():
#                 return False
#         return True if not stack else False