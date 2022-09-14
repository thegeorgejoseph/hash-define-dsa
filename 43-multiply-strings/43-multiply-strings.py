class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,  num2]: return "0"
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = res[i + j] + (int(num1[i]) * int(num2[j]))
                res[i + j + 1] += temp // 10 
                res[i + j] = temp % 10
        
        res = res[::-1]
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        return "".join(map(str, res[i:]))