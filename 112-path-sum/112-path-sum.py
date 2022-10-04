# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, sumSoFar):
            if not node:
                return None
            
            sumSoFar += node.val
            left = dfs(node.left, sumSoFar)
            right = dfs(node.right, sumSoFar)
            if left is True or right is True:
                return True
            if left is False and right is False:
                return False
            if left is None and right is None:
                return sumSoFar == targetSum
            
            return False

        return dfs(root, 0)