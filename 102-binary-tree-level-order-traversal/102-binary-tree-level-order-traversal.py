# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # just like bfs using a queue but instead of adding directly you add after you
        # have processed all the nodes in a level because otherwise we will lose track of what 
        # is there
        res = []
        q = collections.deque([])
        if root: q.append(root)
        while len(q):
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res
            