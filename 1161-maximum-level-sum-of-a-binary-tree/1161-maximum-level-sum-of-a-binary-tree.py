# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        currentLevel = 1
        queue = deque([root])
        maxSum = root.val
        maxLevel = 1
        while queue:
            level = []
            for i in range(len(queue)):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                level.append(top.val)
            if sum(level) > maxSum:
                maxSum = sum(level)
                maxLevel = currentLevel
            currentLevel += 1
        return maxLevel