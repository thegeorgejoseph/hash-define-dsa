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