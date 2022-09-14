class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        res = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            visit.add(course)
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            graph[course] = []
            res.append(course)
            return True
        
        for course, pre in graph.items():
            if not dfs(course): return []
        
        return res