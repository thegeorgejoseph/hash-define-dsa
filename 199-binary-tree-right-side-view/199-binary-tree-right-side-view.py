# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                top = queue.popleft()
                level.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
            res.append(level[-1])
        return res