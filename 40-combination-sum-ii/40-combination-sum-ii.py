class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
                
        backtrack([], 0, target)
        return res
        
#         Follow this for interviews
        # res = []
        # combination = []
        # candidates.sort()
        # def dfs(i, total):
        #     if total == target:
        #         res.append(combination[:]) #without this everything fails because call by reference
        #         return
        #     if i >= len(candidates):
        #         return 
        #     combination.append(candidates[i])
        #     dfs(i+1,total + candidates[i])
        #     combination.pop()
        #     while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
        #         i += 1
        #     dfs(i+1,total)
        # dfs(0,0)
        # return res
            