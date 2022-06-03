# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthRecurse(self,node,depth):
        if not node:
            return depth
        leftMax = self.maxDepthRecurse(node.left, depth + 1)
        rightMax = self.maxDepthRecurse(node.right, depth + 1)
        
        return max(leftMax, rightMax)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.maxDepthRecurse(root, 0)
        