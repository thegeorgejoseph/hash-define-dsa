class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visit = set()
        lastIdx = {c : i for i, c in enumerate(s)}
        for i, char in enumerate(s):
            if char not in visit:
                while stack and char < stack[-1] and i < lastIdx[stack[-1]]:
                    visit.remove(stack.pop())
                visit.add(char)
                stack.append(char)
        return "".join(stack)