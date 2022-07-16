# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, res):
        if not node:
            return 0
        
        left = self.dfs(node.left, res)
        right = self.dfs(node.right, res)
        
        if abs(left - right) > 1:
            res[0] = False
            
        return max(left + 1, right + 1)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        
        self.dfs(root, res)
        return False if res[0] == False else True