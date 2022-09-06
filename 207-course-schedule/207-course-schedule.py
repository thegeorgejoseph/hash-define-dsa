class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if not preMap[course]:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            preMap[course] = []
            cycle.remove(course)
            return True
              
        for course, pre in preMap.items():
            if not dfs(course):
                return False
        
        return True