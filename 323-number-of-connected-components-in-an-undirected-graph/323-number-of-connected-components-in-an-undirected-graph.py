class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        res = n
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res
#         hashmap = collections.defaultdict(list)
#         for i,j in edges:
#             hashmap[i].append(j)
#         visit = set()
        
#         def dfs(n):
#             if n in visit:
#                 return False
            
#             visit.add(n)
#             for nei in hashmap[n]:
#                 dfs(nei)
         
#         res = 0
#         for n1,n2 in edges:
#             if n1 not in visit:
#                 res += 1
#                 dfs(n1)
#         print(visit)
#         print(res)
#         return res if len(visit) == n else (n - len(visit) + res)