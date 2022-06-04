# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, res):
        if  res[0] == False:
            return 0
        if not node:
            return 0
        
        left = self.dfs(node.left,res)
        right = self.dfs(node.right,res)
        
        if abs(right - left) > 1:
            res[0] = False
            
        return max(left + 1,right + 1)
    
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # for every node being traversed back up we need to calculate the height of the lefttree, righttree and the max of both that should be returned back up to the parent
        res = [True]
        
        self.dfs(root,res)
        return res[0]