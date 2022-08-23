class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = {i: [] for i in range(numCourses)}
        cycle = set()
        for crs, pre in prerequisites:
            cache[crs].append(pre)
        
        def dfs(course):
            if course in cycle:
                return False
            if not cache[course]:
                return True
            
            cycle.add(course)
            for pre in cache[course]:
                if not dfs(pre): return False
            
            cycle.remove(course)
            cache[course] = []
            return True
        
        
        for course, pre in prerequisites:
            if not dfs(course): return False
        
        return True