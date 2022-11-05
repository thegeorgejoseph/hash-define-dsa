# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, sumSoFar):
            if not node:
                return False
            
            sumSoFar += node.val
            if not node.left and not node.right:
                return sumSoFar == targetSum
            
            if dfs(node.left, sumSoFar): return True
            if dfs(node.right, sumSoFar): return True
            
            return False
        
        return dfs(root, 0)