class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        res = []
        cycle, visit = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            visit.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            res.append(course)
            return True
        
        for crs, _ in graph.items():
            if not dfs(crs): 
                return []
        
        return res if len(res) == numCourses else []
        
        