# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = collections.deque([root])
        while stack:
            top = stack.pop()
            if p.val < top.val and q.val < top.val:
                stack.append(top.left)
            elif p.val > top.val and q.val > top.val:
                stack.append(top.right)
            else:
                return top
        