# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         iterative solutions are almost always better as long as you can do it
#         no performance gain in this scenario because simple problem statement

#         if not root:
#             return None
        
#         queue = collections.deque([root])
#         while queue:
#             current = queue.popleft()
#             current.left, current.right = current.right, current.left
#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)
        
#         return root

#         recursive solution of a tree
#         O(n) time because every node has to be visited once, O(n) space because O(h) call stack and h == n in this scenario because everything will be in the call stack once.
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        
        return root
        
        