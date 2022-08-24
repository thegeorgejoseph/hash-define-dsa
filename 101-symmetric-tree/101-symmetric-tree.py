# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            
            
            return n1.val == n2.val and dfs(n1.right, n2.left) and dfs(n2.right, n1.left)
        
        return dfs(root,root)