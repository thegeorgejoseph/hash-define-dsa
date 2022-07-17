# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        res = []
        if not root:
            return res
        while queue:
            level = []
            for _ in range(len(queue)):
                top = queue.popleft()
                level.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
            res.append(level)
        
        return res
            