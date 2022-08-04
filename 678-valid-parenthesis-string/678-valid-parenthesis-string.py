class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeftPar, maxLeftPar = 0,0
        for char in s:
            if char == '(':
                minLeftPar += 1
                maxLeftPar += 1
            elif char == ')':
                minLeftPar -= 1
                maxLeftPar -= 1
            else:
                minLeftPar -= 1
                maxLeftPar += 1
            if minLeftPar < 0:
                minLeftPar = 0
            if maxLeftPar < 0:
                return False
        return minLeftPar == 0
