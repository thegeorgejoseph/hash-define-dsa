# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                print(node.val)
                return node.val
            right = dfs(node.right)
            return left or right 
        
        return dfs(root)