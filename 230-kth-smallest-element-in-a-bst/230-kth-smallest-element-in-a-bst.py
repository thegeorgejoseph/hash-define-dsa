# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        self.i = 0
        current = stack[-1]
        while stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            self.i += 1
            if self.i == k:
                return current.val
            current = current.right 