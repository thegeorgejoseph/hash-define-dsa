"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        if not node:
            return None
        
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            hashmap[node] = Node(node.val)
            for n in node.neighbors:
                hashmap[node].neighbors.append(dfs(n))
            
            return hashmap[node]
        
        
        return dfs(node)