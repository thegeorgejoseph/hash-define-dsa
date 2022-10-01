class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, comb, total):
            if i == len(candidates) or total > target:
                return
            if total == target:
                res.append(comb[:])
                return
            
            
            comb.append(candidates[i])
            dfs(i, comb, total + candidates[i])
            comb.pop()
            dfs(i + 1, comb, total)
            
        dfs(0, [], 0)
        return res