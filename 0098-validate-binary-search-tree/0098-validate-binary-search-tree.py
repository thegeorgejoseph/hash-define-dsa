# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lowerBound, upperBound):
            if not node:
                return True
            if not (node.val > lowerBound and node.val < upperBound):
                return False
            
            left = dfs(node.left, lowerBound, node.val)
            right = dfs(node.right, node.val, upperBound)
            
            if not left or not right:
                return False
            
            return True
        
        return dfs(root, float('-inf'), float('inf'))
        