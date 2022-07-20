class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, total, subset):
            if total == target:
                res.append(subset[:])
                return
            if i == len(candidates) or total > target:
                return 
            subset.append(candidates[i])
            backtrack(i + 1, total + candidates[i], subset)
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, total, subset)
        backtrack(0,0,[])
        return res
