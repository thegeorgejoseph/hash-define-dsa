# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left is None or right is None:
                return None
            if left != 0 and right != 0:
                self.res = left + right
                return None
            if (left != 0 or right != 0) and (node.val == p or node.val == q):
                self.res = left if left != 0 else right
                return None
            if left != 0:
                return left + 1
            if right != 0:
                return right + 1
            if node.val == p or node.val == q:
                return left + right + 1
            return 0
        
        dfs(root)
        return self.res