# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([])
        if root: q.append(root)
        while len(q):
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level[-1].val)
        return res