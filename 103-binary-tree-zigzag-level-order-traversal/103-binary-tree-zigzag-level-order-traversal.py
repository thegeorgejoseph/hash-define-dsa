# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        isRight = True
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                level.append(top.val)
            if isRight:
                res.append(level)
            else:
                res.append(level[::-1])
            isRight = not isRight
        return res