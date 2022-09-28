# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower, upper):
            if not node: return True
            if not (node.val > lower and node.val < upper): return False
            
            left = dfs(node.left, lower, node.val)
            right = dfs(node.right, node.val, upper)
            
            return left and right
        
        return dfs(root, float('-inf'), float('inf'))