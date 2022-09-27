class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        avail = set(["(","[", "{"])
        
        for char in s:
            if char in avail:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False
                