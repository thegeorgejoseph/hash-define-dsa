class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyMap = {i : [] for i in range(numCourses)}
        visit = set()
        for course, prereq in prerequisites:
            dependencyMap[course].append(prereq)
        
        def backtrack(course):
            if course in visit:
                return False
            if not dependencyMap[course]:
                return True
            visit.add(course)
            for crs in dependencyMap[course]:
                if not backtrack(crs): return False
            visit.remove(course)
            dependencyMap[course] = []
            return True
            
            
            
        for course, _ in dependencyMap.items():
            if not backtrack(course): return False
        return True