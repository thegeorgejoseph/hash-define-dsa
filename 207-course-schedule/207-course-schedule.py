class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : []  for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if len(graph[course]) == 0:
                return True
            
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            graph[course] = []
            return True
        
        
        for course, _ in graph.items():
            if not dfs(course): return False
        
        return True