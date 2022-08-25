class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res= [] 
        candidates.sort()
        
        def dfs(i, comb, total):
            if total == target:
                res.append(comb[:])
                return 
            if i == len(candidates) or total > target:
                return 
            
            comb.append(candidates[i])
            dfs(i + 1, comb, total + candidates[i])
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, comb, total)
            
            return 
        
        dfs(0, [], 0)
        return res
