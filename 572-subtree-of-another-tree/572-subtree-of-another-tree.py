# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, one, two):
        if not one and not two:
            return True
        if not one or not two:
            return False
        if one.val == two.val and self.isSameTree(one.left, two.left) and self.isSameTree(one.right, two.right):
            return True
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
#         The mistake being made was that 