# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        def dfs(node, curDepth):
            if not node or curDepth == depth:
                return
            if curDepth == depth -1:
                leftTemp = node.left
                rightTemp = node.right
                node.left = TreeNode(val, leftTemp, None)
                node.right = TreeNode(val, None, rightTemp)
            
            dfs(node.left, curDepth + 1)
            dfs(node.right, curDepth + 1)
        
        dfs(root, 1)
        return root