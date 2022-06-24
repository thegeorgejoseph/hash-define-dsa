class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        # for i in range(numCourses):
        #     preMap[i] = []
        visit = set()
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        
        def dfs(course):
            if course in visit:
                return False
            if not preMap[course]:
                return True
            
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visit.remove(course) # so that we can check for other cycles
            preMap[course] = [] # so that we know that this one has no pre reqs
            return True
        
        for key, values in preMap.items():
            if not dfs(key): return False
        return True