class Solution:
    def isValid(self, s: str) -> bool:
        cache = { ")": "(", "}":"{","]":"["}
        open_set = set(["(","[","{"])
        stack = deque()
        for char in s:
            if char in open_set:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if cache[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False