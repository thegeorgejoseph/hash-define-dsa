class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        for i,c in enumerate(s):
            counter[c] = i
        res = []
        maxRight = counter[s[0]]
        left = 0
        for i in range(1,len(s)):
            if i > maxRight:
                res.append(maxRight - left + 1)
                left = i 
            maxRight = max(maxRight, counter[s[i]])
        
        res.append(maxRight - left + 1)
        return res