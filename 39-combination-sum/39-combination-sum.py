class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, current):
            if total == target:
                res.append(current.copy())
                return 
            if i == len(candidates) or total > target:
                return
            #choosing to add it
            current.append(candidates[i])
            dfs(i, total + candidates[i], current)
            #not choosing to add it anymore
            current.pop()
            dfs(i+1, total, current)
        dfs(0,0,[])
        return res