class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        components = n 
        parent = [i for i in range(n)]
        rank = [1] * n
        
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
            
            return 1
        for v1,v2 in edges:
            if not union(v1,v2):
                return False
            else: 
                components -= 1
        
        return True if components == 1 else False