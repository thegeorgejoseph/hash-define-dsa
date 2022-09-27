# while stack is not empty and current character is lexicographically smaller than previous character and there is another item of the previous character
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdx = {c: i for i, c in enumerate(s)}
        cache = set()
        stack = []
        for i, c in enumerate(s):
            if c in cache:
                continue
            while stack and i < lastIdx[stack[-1]] and c < stack[-1]:
                top = stack.pop()
                cache.remove(top)          
            else:
                cache.add(c)
                stack.append(c)
        return "".join(stack)