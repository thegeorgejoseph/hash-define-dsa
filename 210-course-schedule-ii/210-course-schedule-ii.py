class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle, visit = set(), set()
        res = []
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            
            cycle.add(course)
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            preMap[course] = []
            res.append(course)
            cycle.remove(course)
            return True
        
        
        for course, _ in preMap.items():
            if not dfs(course): return []
        
        return res