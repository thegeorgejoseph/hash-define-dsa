# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, one, two):
        if not one and not two:
            return True
        
        if not one or not two:
            return False
        
        left = self.dfs(one.left, two.left)
        right = self.dfs(one.right, two.right)
        
        if left == False or right == False or one.val != two.val:
            return False
        
        return True
        
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
        