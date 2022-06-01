class Solution:
#     create test cases before starting to code
# valid case : [], [()]
# invalid case: ][, [), [, ]
    def isValid(self, s: str) -> bool:
        map = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for char in s:
            if char in map:
                if not stack:
                    return False
                if stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False