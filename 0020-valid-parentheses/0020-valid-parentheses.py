class Solution:
    def isValid(self, s: str) -> bool:
        cache = {")":"(", "]":"[", "}": "{"}
        stack = []
        for char in s:
            if char not in "([{":
                if not stack or stack[-1] != cache[char]: return False
                stack.pop()
            else:
                stack.append(char)
        return True if len(stack) == 0 else False