# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(t1, t2):
            if not t1 and not t2:
                return None
            
            value1 = t1.val if t1 else 0
            value2 = t2.val if t2 else 0
            
            root = TreeNode(value1 + value2)
            root.left = dfs(t1.left if t1 else None, t2.left if t2 else None)
            root.right = dfs(t1.right if t1 else None, t2.right if t2 else None)
            
            return root
        
        return dfs(root1, root2)
    