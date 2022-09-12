"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        copy = {}
        
        def dfs(node):
            if not node or node in copy:
                return 
            
            copy[node] = Node(node.val,None)
            for nei in node.neighbors:
                dfs(nei)
                copy[node].neighbors.append(copy[nei])
        
        dfs(node)
        return copy[node]