class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        cycle = set()
        
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        def backtrack(course):
            if course in cycle:
                return False
            if not graph[course]:
                return True
            
            cycle.add(course)
            for pre in graph[course]:
                if not backtrack(pre): return False
            
            cycle.remove(course)
            graph[course] = []
            return True
        
        
        
        for course, pre in graph.items():
            if not backtrack(course): return False
        
        return True