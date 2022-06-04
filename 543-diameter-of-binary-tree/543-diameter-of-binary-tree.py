# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node,res):
        if not node:
                return 0
            
        left = self.dfs(node.left,res)
        right = self.dfs(node.right,res)

        res[0] = max(res[0], left + right)

        return max(left + 1, right + 1)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0] #global variable that is being accessed by the recursive function
        
        #why did I add a + 1 there because at every point when the node returns something back to its parent you need to add 1 because that is the number of number of nodes under the parent
        self.dfs(root,res)
        return res[0]