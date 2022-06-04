# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     Iterative BFS - Queue
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([[root,1]])
        max_depth = 0
        while queue:
            current = queue.popleft()
            if current[0].left:
                queue.appendleft([current[0].left,current[1]+ 1])
            if current[0].right:
                queue.appendleft([current[0].right,current[1] + 1])
            max_depth = max(current[1], max_depth)
            
        return max_depth
#     Iterative DFS - Stack
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         max_depth = 0
#         stack = collections.deque([[root,1]])
#         while stack:
#             current = stack.pop()
#             if current[0].left:
#                 stack.append([current[0].left,current[1] + 1])
#             if current[0].right:
#                 stack.append([current[0].right,current[1] + 1])
                
#             max_depth = max(max_depth, current[1])
#         return max_depth
        
        
        
        
        
#     Recursive DFS solution is not that great because 
#     def maxDepthRecurse(self,node,depth):
#         if not node:
#             return depth
#         leftMax = self.maxDepthRecurse(node.left, depth + 1)
#         rightMax = self.maxDepthRecurse(node.right, depth + 1)
        
#         return max(leftMax, rightMax)
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return self.maxDepthRecurse(root, 0)
        