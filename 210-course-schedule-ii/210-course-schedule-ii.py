class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        res = []
        visit, cycle = set(), set()
        
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        
        def backtrack(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            visit.add(course)
            for pre in graph[course]:
                if not backtrack(pre): return False
            
            cycle.remove(course)
            res.append(course)
            graph[course] = []
            return True
        
        
        for crs, pre in graph.items():
            if not backtrack(crs): return []
        
        return res