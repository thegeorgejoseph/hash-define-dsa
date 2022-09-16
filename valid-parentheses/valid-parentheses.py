class Solution:
    def isValid(self, s: str) -> bool:
        cache = {")":"(", "]":"[","}":"{"}
        stack = []
        openbracks = set(["(","[","{"])
        for bracket in s:
            if bracket in openbracks:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] != cache[bracket]:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False
            