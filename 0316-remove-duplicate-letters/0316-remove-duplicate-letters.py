# set to keep track of all the letters that in the solution
# stack to keep track of the solution
# pop from the stack if the current letter is lexicographically smaller than the one before it and there is another one of it that can be used later
# do not attempt to remove anything if character is already in the solution set
# we need the lastIdx of all characters in the string to be able to find if it can be removed
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i
        stack = []
        visit = set()
        for i, char in enumerate(s):
            if char in visit:
                continue
            while stack and char < stack[-1] and i < lastIdx[stack[-1]]:
                top = stack.pop()
                visit.remove(top)
            else:
                visit.add(char)
                stack.append(char)
        return "".join(stack)
                