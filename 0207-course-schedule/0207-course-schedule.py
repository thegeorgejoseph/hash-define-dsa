class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        cycle = set()
        
        def dfs(course):
            if course in cycle: 
                return False
            if not graph[course]:
                return True
            
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            graph[course] = []
            return True
            
            
        
        for crs, _ in graph.items():
            if not dfs(crs): return False
        
        return True 