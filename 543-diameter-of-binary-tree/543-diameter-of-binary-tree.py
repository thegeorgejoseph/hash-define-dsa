# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, res):
        if not node:
            return -1
        leftHeight = self.dfs(node.left, res)
        rightHeight = self.dfs(node.right, res)
        res[0] = max(res[0], leftHeight + rightHeight + 2)
        
        return max(leftHeight + 1, rightHeight +1 )
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        self.dfs(root, res)
        return res[0]