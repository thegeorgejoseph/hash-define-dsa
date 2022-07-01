class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        index = {}
        for i,c in enumerate(s):
            index[c] = i
        
        maxIdxSoFar = index[s[0]]
        left = -1
        for i, c in enumerate(s):
            if i > maxIdxSoFar:
                res.append(maxIdxSoFar - left)
                left = maxIdxSoFar
            maxIdxSoFar = max(maxIdxSoFar, index[c])
                
        res.append(maxIdxSoFar - left)
        return res
            
                    
            