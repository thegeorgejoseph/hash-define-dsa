"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        cache = {None: None}
        
        def dfs(node):
            if node in cache:
                return cache[node]
            
            cache[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)
            
            for nei in node.neighbors:
                cache[node].neighbors.append(cache[nei])
        
        dfs(node)
        return cache[node]