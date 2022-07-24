class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencyMap = {i: [] for i in range(numCourses)}
        visited, cycle = set(), set()
        res = []
        for crs, dep in prerequisites:
            dependencyMap[crs].append(dep)
            
        def backtrack(course):
            if course in cycle: return False
            if course in visited: return True
            
            visited.add(course)
            cycle.add(course)
            
            for dep in dependencyMap[course]:
                if not backtrack(dep): return False
            
            cycle.remove(course)
            res.append(course)
            dependencyMap[course] = []
            return True
            
            
            
        
        for course, _ in dependencyMap.items():
            if not backtrack(course): return []
        
        return res
        
        
        
        
#         preMap = {i:[] for i in range(numCourses)}
#         for cur, pre in prerequisites:
#             preMap[cur].append(pre)
            
#         visit, cycle = set(), set()
#         # we have a visit set here instead of changing the prereq to []
#         res = []
        
#         def dfs(course):
#             if course in cycle: # In cycle so False
#                 return False
#             if course in visit: #already visited so True
#                 return True
            
#             cycle.add(course)
#             for pre in preMap[course]:
#                 if not dfs(pre): return False
#             cycle.remove(course)
#             visit.add(course)
#             res.append(course)
#             return True
        
#         for course in range(numCourses):
#             if not dfs(course): return []
#         return res