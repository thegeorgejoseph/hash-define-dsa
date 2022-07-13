class Solution:
    def isValid(self, s):
        _ascii = ord(s)
        if _ascii >= 97 and _ascii <= 122:
            return s
        if _ascii >= 65 and _ascii <= 90:
            return chr(_ascii + 32)
        if _ascii >= 48 and _ascii <= 57:
            return s
        return "invalid"
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left <= right:
            leftChar = self.isValid(s[left])
            rightChar = self.isValid(s[right])
            if leftChar == "invalid":
                left += 1
                continue
            if rightChar == "invalid":
                right -= 1
                continue
            if leftChar != rightChar:
                return False
            left += 1
            right -= 1
        return True