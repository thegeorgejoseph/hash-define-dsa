# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxSoFar):
            if not node:
                return 0
            
            left = dfs(node.left, max(maxSoFar, node.val))
            right = dfs(node.right, max(maxSoFar, node.val))
            
            if maxSoFar > node.val:
                return left + right
            else:
                return left + right + 1
            
        return dfs(root, root.val)
        
        
        