class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = version1.split(".")
        n2 = version2.split(".")
        
        for i in range(max(len(n1),len(n2))):
            num1 = int(n1[i]) if i < len(n1) else 0
            num2 = int(n2[i]) if i < len(n2) else 0
            if num1 != num2:
                return 1 if num1 > num2 else -1
        
        return 0