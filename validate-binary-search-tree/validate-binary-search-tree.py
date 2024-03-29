# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            if not (node.val > leftBound and node.val < rightBound):
                return False
            left = dfs(node.left, leftBound, min(rightBound, node.val))
            right = dfs(node.right, max(leftBound, node.val), rightBound)
            
            return left and right
        
        return dfs(root, float("-inf"), float("inf"))
