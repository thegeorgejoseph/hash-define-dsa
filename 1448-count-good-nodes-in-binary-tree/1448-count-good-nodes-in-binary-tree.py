# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #solution without extra space
        def dfs(node, max_so_far):
            if not node:
                return 0
            left = dfs(node.left, max(max_so_far, node.val))
            right = dfs(node.right, max(max_so_far, node.val))
            res = left + right
            res += 1 if max_so_far <= node.val else 0
            return res
        return dfs(root, root.val)
        #This is using extra memory even though the time complexity is not affected, lets try passing the solution up
#         count = [0]
#         def dfs(node, max_so_far,count):
#             if not node:
#                 return
#             left = dfs(node.left, max(max_so_far, node.val),count)
#             right = dfs(node.right, max(max_so_far, node.val),count)
            
#             if max_so_far <= node.val:
#                 count[0] += 1
#         dfs(root, root.val,count)
#         return count[0]