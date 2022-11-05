# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.word = []
        def dfs(node):
            if not node:
                return 
            
            self.word.append("(")
            self.word.append(node.val)
            if not node.left and node.right:
                self.word.append("()")
            dfs(node.left)
            dfs(node.right)
            self.word.append(")")
        
            
        dfs(root)
        return "".join(map(str, self.word[1:-1]))
            