# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = deque([(root,1)])
        res = 0
        while stack:
            top,depth = stack.pop()
            res = max(res, depth)
            if top.left:
                stack.append((top.left, depth + 1))
            if top.right:
                stack.append((top.right, depth + 1))
        return res
            
        # if not root:
        #     return 0
        # res = 0
        # queue = deque([root])
        # while queue:
        #     for i in range(len(queue)):
        #         top = queue.popleft()
        #         if top.left:
        #             queue.append(top.left)
        #         if top.right:
        #             queue.append(top.right)
        #     res += 1
        # return res
        
#         def dfs(node):
#             if not node:
#                 return 0
            
#             left = dfs(node.left)
#             right = dfs(node.right)
            
#             return max(left, right)  + 1
        
#         return dfs(root)