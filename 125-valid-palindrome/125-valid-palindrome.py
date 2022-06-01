class Solution:
    def isValidCharacter(self, char):
        ascii_char = ord(char)
        if ascii_char >= 97 and ascii_char <= 122:
            return char
        elif ascii_char >= 65 and ascii_char <= 90:
            return chr(ascii_char + 32)
        elif ascii_char >=48 and ascii_char <=57:
            return char
        else:
            return "Invalid"
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0 or n == 1:
            return True
        start = 0
        end = n -1 
        while start <= end:
            first = self.isValidCharacter(s[start])
            last = self.isValidCharacter(s[end])
            print(f" First - {s[start]} :: {first}")
            print(f"Last - {s[end]} :: {last}")
            if first == "Invalid":
                start += 1
                continue
            if last == "Invalid":
                end -= 1
                continue
            if first == last:
                start += 1
                end -= 1
                continue
            else:
                return False
        
        return True