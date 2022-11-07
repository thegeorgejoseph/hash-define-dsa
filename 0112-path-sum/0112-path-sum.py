# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, _sum):
            if not node:
                return False
            
            _sum += node.val
            if not node.left and not node.right:
                return _sum == targetSum
            if dfs(node.left, _sum):
                return True
            if dfs(node.right, _sum):
                return True
            
            return False
        
        return dfs(root, 0)