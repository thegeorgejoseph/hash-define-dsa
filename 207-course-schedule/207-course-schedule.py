class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if not graph[course]:
                return True
            visit.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            visit.remove(course)
            graph[course] = []
            return True

        
        for course, pre in graph.items():
            if not dfs(course): return False
        
        return True