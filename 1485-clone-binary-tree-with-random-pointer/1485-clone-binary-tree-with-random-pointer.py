# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        cache = {None: None}
        
        def dfs(node):
            if not node:
                return 
            
            if node not in cache:
                cache[node] = NodeCopy(node.val)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        def setConnections(node):
            if not node:
                return 
            
            cache[node].left = cache[node.left]
            cache[node].right = cache[node.right]
            cache[node].random = cache[node.random]
            setConnections(node.left)
            setConnections(node.right)
        
        setConnections(root)
        return cache[root]
            